from flask import Flask, render_template, request, jsonify, session
import requests
import os
from dotenv import load_dotenv
import sqlite3
from datetime import datetime
import json
import hashlib
import time
import sys
import random
import logging

# Set up logging for better error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Validate required environment variables
SESSION_SECRET = os.environ.get('SESSION_SECRET')
if not SESSION_SECRET:
    logging.error("SESSION_SECRET environment variable is required but not set.")
    sys.exit(1)

app.secret_key = SESSION_SECRET

# Optional API Keys (only for reverse geocoding, weather, and air quality display)
OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY')

# API Response Cache (in-memory caching for optimization)
API_CACHE = {}
CACHE_DURATION = 300  # 5 minutes in seconds

# ======================================================================================
# ACCURATE REAL-WORLD EMISSION FACTOR TABLES
# ======================================================================================

# State-specific electricity emission factors (kg CO2 per kWh) - US EPA 2023 data
STATE_ELECTRICITY_FACTORS = {
    'India': 0.708,

    # Indian States
    'Andhra Pradesh': 0.690,
    'Arunachal Pradesh': 0.420,
    'Assam': 0.520,
    'Bihar': 0.740,
    'Chhattisgarh': 0.850,
    'Goa': 0.280,
    'Gujarat': 0.680,
    'Haryana': 0.720,
    'Himachal Pradesh': 0.030,
    'Jharkhand': 0.880,
    'Karnataka': 0.690,
    'Kerala': 0.120,
    'Madhya Pradesh': 0.760,
    'Maharashtra': 0.720,
    'Manipur': 0.350,
    'Meghalaya': 0.310,
    'Mizoram': 0.220,
    'Nagaland': 0.270,
    'Odisha': 0.780,
    'Punjab': 0.710,
    'Rajasthan': 0.730,
    'Sikkim': 0.040,
    'Tamil Nadu': 0.650,
    'Telangana': 0.705,
    'Tripura': 0.330,
    'Uttar Pradesh': 0.760,
    'Uttarakhand': 0.050,
    'West Bengal': 0.680,

    # Union Territories
    'Delhi': 0.730,
    'Puducherry': 0.250,
    'Chandigarh': 0.180,
    'Jammu and Kashmir': 0.420,
    'Ladakh': 0.340,
    'Andaman and Nicobar Islands': 0.210,
    'Lakshadweep': 0.260,
    'Dadra and Nagar Haveli and Daman and Diu': 0.390
}

# Transport emission factors (kg CO2 per km) - IPCC 2023 & EPA data
TRANSPORT_FACTORS = {
    'walk': 0.0,
    'bicycle': 0.0,
    'public': 0.041,      # Public transport (bus/metro average)
    'car': 0.192,         # Average gasoline car
    'car_small': 0.145,   # Small car
    'car_medium': 0.192,  # Medium car
    'car_large': 0.245,   # Large car/SUV
    'suv': 0.245,         # SUV
    'motorcycle': 0.103,  # Motorcycle
    'electric_car': 0.053, # Electric car (includes grid emissions)
    'hybrid': 0.119,      # Hybrid car
    'train': 0.041,       # Train
    'metro': 0.031,       # Metro/subway
    'bus': 0.089,         # Bus
    'airplane_short': 0.255, # Short-haul flight per km
    'airplane_long': 0.195   # Long-haul flight per km
}

# Industries emission factors (kg CO2 per month) - Based on EPA industrial sector data
INDUSTRIES_FACTORS = {
    'low': 120,      # Minimal industrial footprint (remote work, digital services)
    'medium': 280,   # Average office/retail/light manufacturing
    'high': 580      # Heavy manufacturing, industrial facilities
}

# Waste emission factors (kg CO2 per kg of waste) - EPA WARM Model 2023
WASTE_FACTORS = {
    'recycling_rate': {
        'high_recycling': 0.42,    # >50% recycling rate
        'medium_recycling': 0.89,  # 20-50% recycling rate
        'low_recycling': 1.54      # <20% recycling rate
    },
    'waste_type_avg': 0.89  # Average mixed municipal solid waste
}

# Average monthly waste generation (kg per month)
AVERAGE_WASTE_MONTHLY = {
    'minimal': 30,    # <10 kg/week = ~40 kg/month
    'average': 60,    # ~15 kg/week = ~60 kg/month
    'high': 100       # >20 kg/week = ~100 kg/month
}

# ======================================================================================
# DATABASE SETUP
# ======================================================================================

def init_db():
    conn = sqlite3.connect('eco_twin.db')
    c = conn.cursor()
    
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    # Calculations history (diet field represents industries data)
    c.execute('''CREATE TABLE IF NOT EXISTS calculations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        electricity REAL,
        transport REAL,
        diet REAL,
        waste REAL,
        total_co2 REAL,
        category TEXT,
        region TEXT,
        input_mode TEXT,
        calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        latitude REAL,
        longitude REAL,
        city_name TEXT,
        state_name TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )''')
    
    # User stats table
    c.execute('''CREATE TABLE IF NOT EXISTS user_stats (
        user_id INTEGER PRIMARY KEY,
        total_points INTEGER DEFAULT 0,
        eco_twin_happiness INTEGER DEFAULT 50,
        tree_level INTEGER DEFAULT 1,
        current_tree_stage INTEGER DEFAULT 1,
        total_calculations INTEGER DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )''')
    
    # Add state_name column if it doesn't exist
    try:
        c.execute("ALTER TABLE calculations ADD COLUMN state_name TEXT")
        conn.commit()
    except sqlite3.OperationalError:
        pass
    
    # Add current_tree_stage column if it doesn't exist
    try:
        c.execute("ALTER TABLE user_stats ADD COLUMN current_tree_stage INTEGER DEFAULT 1")
        conn.commit()
    except sqlite3.OperationalError:
        pass
    
    conn.commit()
    conn.close()

init_db()

# Helper function to get or create default user
def get_default_user():
    conn = sqlite3.connect('eco_twin.db')
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username = 'default_user'")
    user = c.fetchone()
    
    if not user:
        c.execute("INSERT INTO users (username, email) VALUES (?, ?)", 
                  ('default_user', 'user@ecotwin.com'))
        conn.commit()
        user_id = c.lastrowid
        c.execute("INSERT INTO user_stats (user_id) VALUES (?)", (user_id,))
        conn.commit()
    else:
        user_id = user[0]
    
    conn.close()
    return user_id

# Enhanced Eco-Facts for Daily Life
ECO_FACTS = [
    {"fact": "💡 Turning off lights while studying saves energy and reduces carbon — it's like skipping one car trip every week!", "action_tip": "Place sticky notes on switches. It becomes a habit in 21 days!", "analogy": "If every household turned off one bulb, we'd save energy to light 3 million homes yearly."},
    {"fact": "🍳 Cooking with a lid on saves up to 30% of the gas or electricity — less energy, same tasty food!", "action_tip": "Always cover pots when boiling water or cooking. Time yourself - it cooks faster too!", "analogy": "Using a lid while cooking saves enough energy monthly to charge your phone for a year."},
    {"fact": "🚶‍♀️ Walking to nearby shops or college burns calories and cuts your transport emissions in half.", "action_tip": "Start with one walking trip per week - maybe your coffee run or grocery stops.", "analogy": "Walking 1 mile instead of driving saves emissions equal to 2,000 breaths of fresh air."},
    {"fact": "🧴 Turning off the tap while washing your face or brushing saves 6 liters of water every minute.", "action_tip": "Use a mug for brushing. You'll save enough water to provide drinking water for one person for 3 days weekly.", "analogy": "A running tap wastes 6 liters per minute - that's 12 water bottles down the drain!"},
    {"fact": "🌳 Spending time in the park boosts mental health — and parks absorb thousands of kilograms of CO₂ yearly.", "action_tip": "Visit a local park once a week. Combine it with walking or jogging for double benefits!", "analogy": "2 mature trees provide enough oxygen for a family of 4 for an entire year."},
    {"fact": "🏋️‍♀️ Going to the gym or dancing at home improves your stamina and lowers your health-related carbon footprint.", "action_tip": "Try 30 minutes of home workouts 3 times a week. You'll save gym transport emissions too!", "analogy": "Home workouts save 520 kg of CO₂ per year compared to driving to the gym daily."},
    {"fact": "☀️ Drying clothes in the sunshine instead of using a dryer saves 1.8 kg of CO₂ per load.", "action_tip": "Use a clothesline or drying rack. Sunlight also naturally disinfects your clothes!", "analogy": "Air-drying clothes for a year saves enough energy to power a TV for 115 hours."},
    {"fact": "🍲 Eating more home-cooked meals instead of takeout cuts plastic waste and delivery fuel emissions.", "action_tip": "Cook double portions and freeze half for later. You'll save time and emissions!", "analogy": "One less takeout meal per week prevents 52 plastic containers from landfills yearly."},
    {"fact": "📱 Using your phone in power-saving mode all day can save the same energy as turning off one bulb for an hour.", "action_tip": "Enable battery saver mode when your phone is above 50%. It also extends battery life!", "analogy": "Power-saving mode on all devices saves enough electricity to light your room for 2 weeks."},
    {"fact": "💻 Keeping your laptop on battery saver during classes reduces energy usage by up to 25%.", "action_tip": "Adjust screen brightness to 70% and close unused tabs. Your battery will thank you too!", "analogy": "Optimizing laptop settings for a year saves enough energy to charge 200 smartphones."},
    {"fact": "🚿 Shortening your shower by 2 minutes saves 18 liters of water — that's enough for a small tree for one week.", "action_tip": "Play a 5-minute playlist. Make it a fun challenge with family!", "analogy": "A 5-minute shower vs 10-minute saves enough water for one person's drinking needs for 12 days."},
    {"fact": "🧘‍♀️ Doing yoga or workouts at home instead of the gym saves travel emissions and keeps you eco-fit.", "action_tip": "Follow free YouTube workouts. You'll save time, money, and emissions!", "analogy": "Working out at home 3 times/week saves 312 kg CO₂/year in transport emissions."},
    {"fact": "🛍️ Carrying your own cloth bag for shopping avoids 500 plastic bags a year.", "action_tip": "Keep 3-4 reusable bags in your car trunk or backpack. Attach one to your keys!", "analogy": "The Great Pacific Garbage Patch is 3x the size of France, largely plastic bags."},
    {"fact": "☕ Using a reusable cup daily can save up to 23 kg of CO₂ in a year.", "action_tip": "Bring your own tumbler to cafes. Many offer discounts for doing so!", "analogy": "156 plastic bottles are saved yearly by using one reusable bottle - enough to circle a city block!"},
    {"fact": "💤 Turning off devices before sleeping saves enough energy to power your fan all night.", "action_tip": "Use power strips. One switch turns off TV, gaming console, and speakers together.", "analogy": "Phantom energy from idle devices costs $165 per household yearly in wasted electricity."}
]

# ======================================================================================
# UTILITY FUNCTIONS
# ======================================================================================

def get_cache_key(prefix, *args):
    """Generate a cache key from prefix and arguments"""
    key_string = f"{prefix}:{':'.join(str(arg) for arg in args)}"
    return hashlib.md5(key_string.encode()).hexdigest()

def get_from_cache(cache_key):
    """Retrieve data from cache if valid"""
    if cache_key in API_CACHE:
        cached_data, timestamp = API_CACHE[cache_key]
        if time.time() - timestamp < CACHE_DURATION:
            logging.info(f"Cache hit for key: {cache_key}")
            return cached_data
        else:
            del API_CACHE[cache_key]
            logging.info(f"Cache expired for key: {cache_key}")
    return None

def set_to_cache(cache_key, data):
    """Store data in cache with timestamp"""
    API_CACHE[cache_key] = (data, time.time())

# ======================================================================================
# GPS & API FUNCTIONS (Only for location display, weather, and air quality)
# ======================================================================================

def reverse_geocode(lat, lon):
    """Get detailed area name from coordinates using OpenStreetMap (free)"""
    cache_key = get_cache_key('geocode', lat, lon)
    cached = get_from_cache(cache_key)
    if cached:
        return cached

    # Default fallback
    default_result = {
        'city': f"{lat:.2f}, {lon:.2f}",
        'state': '',
        'country': '',
        'display': f"{lat:.2f}, {lon:.2f}"
    }

    try:
        # Use Nominatim (OpenStreetMap) for reverse geocoding
        osm_url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
        osm_res = requests.get(osm_url, timeout=5, headers={'User-Agent': 'EcoTwinCalculator/1.0'})
        osm_data = osm_res.json()
        address = osm_data.get('address', {})

        city = (
            address.get('suburb') or
            address.get('neighbourhood') or
            address.get('town') or
            address.get('city') or
            address.get('state_district') or
            'Unknown'
        )
        state = address.get('state', '')
        country = address.get('country', '')

        result = {
            'city': city,
            'state': state,
            'country': country,
            'display': f"{city}, {state}" if state else f"{city}, {country}"
        }

        set_to_cache(cache_key, result)
        return result

    except Exception as e:
        logging.error(f"Geocoding error: {e}")
        set_to_cache(cache_key, default_result)
        return default_result

def fetch_weather(lat, lon):
    """Fetch current weather data from OpenWeatherMap API (optional display only)"""
    cache_key = get_cache_key('weather', round(lat, 2), round(lon, 2))
    cached = get_from_cache(cache_key)
    if cached:
        return cached
    
    # Fallback if no API key
    if not OPENWEATHER_API_KEY:
        return {'temp': 'N/A', 'description': 'No API Key', 'humidity': '--', 'wind_speed': '--', 'source': 'fallback'}
    
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            result = {
                'temp': round(data['main']['temp'], 1),
                'description': data['weather'][0]['description'].capitalize(),
                'humidity': data['main']['humidity'],
                'wind_speed': round(data['wind']['speed'], 1),
                'source': 'live'
            }
            set_to_cache(cache_key, result)
            return result
        logging.error(f"Weather API failed with status code: {response.status_code}")
    except Exception as e:
        logging.error(f"Weather API error: {e}")
    
    return {'temp': 'N/A', 'description': 'API Fail', 'humidity': '--', 'wind_speed': '--', 'source': 'fallback'}

def fetch_air_quality(lat, lon):
    """Fetch air quality data from OpenWeather Air Pollution API (optional display only)"""
    cache_key = get_cache_key('airquality', round(lat, 2), round(lon, 2))
    cached = get_from_cache(cache_key)
    if cached:
        return cached
    
    # Fallback AQI: 3 - Moderate
    fallback_result = {'aqi': 3, 'source': 'fallback'}

    if not OPENWEATHER_API_KEY:
        return fallback_result
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            if 'list' in data and len(data['list']) > 0:
                aqi = data['list'][0]['main']['aqi']  # 1=Good, 5=Very Poor
                result = {'aqi': aqi, 'source': 'live'}
                set_to_cache(cache_key, result)
                return result
        logging.error(f"Air Quality API failed with status code: {response.status_code}")
    except Exception as e:
        logging.error(f"Air Quality API error: {e}")
    
    return fallback_result

# ======================================================================================
# EMISSION CALCULATION FUNCTIONS (Using accurate emission factors)
# ======================================================================================

def get_electricity_factor(state_name, country_name):
    """Get accurate electricity emission factor based on state/country"""
    # Try to match state first (for US states or Indian states)
    if state_name and state_name in STATE_ELECTRICITY_FACTORS:
        factor = STATE_ELECTRICITY_FACTORS[state_name]
        logging.info(f"[ELECTRICITY FACTOR] Using state factor for {state_name}: {factor} kg CO2/kWh")
        return factor
    
    # Try to match country
    if country_name and country_name in STATE_ELECTRICITY_FACTORS:
        factor = STATE_ELECTRICITY_FACTORS[country_name]
        logging.info(f"[ELECTRICITY FACTOR] Using country factor for {country_name}: {factor} kg CO2/kWh")
        return factor
    
    # Global average fallback
    factor = 0.475  # Global average grid emission factor
    logging.info(f"[ELECTRICITY FACTOR] Using global average: {factor} kg CO2/kWh")
    return factor

def calculate_emissions(data):
    """Calculate emissions using accurate real-world emission factors"""
    lat = data.get('lat', 37.7749)
    lon = data.get('lon', -122.4194)
    input_mode = data.get('input_mode', 'question')
    individual_sections = data.get('individual_sections', None)
    
    logging.info(f"[CALCULATE] Starting calculation for location: ({lat}, {lon})")
    if individual_sections:
        logging.info(f"[INDIVIDUAL CALC] Only calculating sections: {individual_sections}")
    
    # Get location details (GPS for location name and state-based electricity adjustment)
    location_info = reverse_geocode(lat, lon)
    state_name = location_info.get('state', '')
    country_name = location_info.get('country', '')
    city_name = location_info.get('city', '')
    
    # Get accurate electricity emission factor based on state/country
    electricity_factor = get_electricity_factor(state_name, country_name)
    
    # Get optional display data (weather and air quality)
    air_quality = fetch_air_quality(lat, lon)
    
    # Initialize variables
    electricity = 0
    transport = 0
    industries = 0
    waste = 0
    
    # Determine which sections to calculate
    calc_all = individual_sections is None or len(individual_sections) == 0
    calc_electricity = calc_all or 'electricity' in individual_sections
    calc_transport = calc_all or 'transport' in individual_sections
    calc_industries = calc_all or 'industries' in individual_sections
    calc_waste = calc_all or 'waste' in individual_sections
    
    # Calculate emissions based on input mode using ACCURATE EMISSION FACTORS
    if input_mode == 'question':
        # Question Mode - Using qualitative inputs with accurate emission factors
        electricity_q = data.get('electricity_q', 'medium')
        transport_q = data.get('transport_q', 'car')
        industries_q = data.get('industries_q', 'medium')
        waste_q = data.get('waste_q', 'average')
        
        # POWERPLANT (Electricity): Use accurate state-based emission factor
        if calc_electricity:
            electricity_map = {'low': 100, 'medium': 300, 'high': 600}  # Monthly kWh estimates
            electricity_kwh = electricity_map.get(electricity_q, 300)
            electricity = electricity_kwh * electricity_factor
            logging.info(f"[ELECTRICITY] {electricity_kwh} kWh × {electricity_factor} kg/kWh = {electricity} kg CO2")
        
        # TRANSPORT: Use accurate transport emission factors
        if calc_transport:
            transport_factor = TRANSPORT_FACTORS.get(transport_q, TRANSPORT_FACTORS['car'])
            transport_km_daily_map = {'walk': 0, 'bicycle': 0, 'public': 10, 'car': 20, 'suv': 30}  # Daily km estimates
            transport_km_daily = transport_km_daily_map.get(transport_q, 20)
            transport_km_monthly = transport_km_daily * 30
            transport = transport_km_monthly * transport_factor
            logging.info(f"[TRANSPORT] {transport_km_daily} km/day × 30 days = {transport_km_monthly} km/month × {transport_factor} kg/km = {transport} kg CO2")
        
        # INDUSTRIES: Use accurate industrial emission factors
        if calc_industries:
            industries = INDUSTRIES_FACTORS.get(industries_q, INDUSTRIES_FACTORS['medium'])
            logging.info(f"[INDUSTRIES] {industries} kg CO2 (level: {industries_q})")
        
        # WASTE: Use accurate waste emission factors
        if calc_waste:
            waste_kg = AVERAGE_WASTE_MONTHLY.get(waste_q, AVERAGE_WASTE_MONTHLY['average'])
            waste_factor = WASTE_FACTORS['waste_type_avg']
            waste = waste_kg * waste_factor
            logging.info(f"[WASTE] {waste_kg} kg waste × {waste_factor} kg CO2/kg = {waste} kg CO2")
        
    else:
        # Number Mode - Using numerical inputs with accurate emission factors
        electricity_n = float(data.get('electricity_n', 300))  # kWh/month
        transport_n = float(data.get('transport_n', 600))      # km/month
        industries_n = float(data.get('industries_n', 280))    # kg CO2/month
        waste_n = float(data.get('waste_n', 60))               # kg/month
        
        # Apply accurate emission factors (only for selected sections)
        if calc_electricity:
            electricity = electricity_n * electricity_factor
            logging.info(f"[ELECTRICITY] {electricity_n} kWh/month × {electricity_factor} kg/kWh = {electricity} kg CO2")
        
        if calc_transport:
            # User provides total monthly km
            transport_factor = TRANSPORT_FACTORS['car']
            transport = transport_n * transport_factor
            logging.info(f"[TRANSPORT] {transport_n} km/month × {transport_factor} kg/km = {transport} kg CO2")
        
        if calc_industries:
            industries = industries_n
            logging.info(f"[INDUSTRIES] {industries} kg CO2/month (direct input)")
        
        if calc_waste:
            # User provides total monthly kg
            waste_factor = WASTE_FACTORS['waste_type_avg']
            waste = waste_n * waste_factor
            logging.info(f"[WASTE] {waste_n} kg/month × {waste_factor} kg CO2/kg = {waste} kg CO2")
    
    total_co2 = electricity + transport + industries + waste
    
    # Individual category thresholds (kg CO2/month)
    ELECTRICITY_THRESHOLDS = {'low': 150, 'medium': 300}  # < 150 = low, < 300 = medium, >= 300 = high
    TRANSPORT_THRESHOLDS = {'low': 80, 'medium': 150}     # < 80 = low, < 150 = medium, >= 150 = high
    INDUSTRIES_THRESHOLDS = {'low': 150, 'medium': 300}   # < 150 = low, < 300 = medium, >= 300 = high
    WASTE_THRESHOLDS = {'low': 40, 'medium': 70}          # < 40 = low, < 70 = medium, >= 70 = high
    
    # Determine category for each section
    def get_category(value, thresholds):
        if value < thresholds['low']:
            return 'low'
        elif value < thresholds['medium']:
            return 'medium'
        else:
            return 'high'
    
    electricity_cat = get_category(electricity, ELECTRICITY_THRESHOLDS) if calc_electricity else 'low'
    transport_cat = get_category(transport, TRANSPORT_THRESHOLDS) if calc_transport else 'low'
    industries_cat = get_category(industries, INDUSTRIES_THRESHOLDS) if calc_industries else 'low'
    waste_cat = get_category(waste, WASTE_THRESHOLDS) if calc_waste else 'low'
    
    # Overall category: use the WORST (highest priority) category among all sections
    # Priority: high > medium > low
    categories = [electricity_cat, transport_cat, industries_cat, waste_cat]
    if 'high' in categories:
        category = 'high'
    elif 'medium' in categories:
        category = 'medium'
    else:
        category = 'low'
    
    logging.info(f"[RESULT] Total CO2: {total_co2} kg/month")
    logging.info(f"[CATEGORIES] Electricity: {electricity_cat}, Transport: {transport_cat}, Industries: {industries_cat}, Waste: {waste_cat}")
    logging.info(f"[OVERALL CATEGORY] {category} (based on worst individual category)")
    
    return {
        'electricity': round(electricity, 2),
        'transport': round(transport, 2),
        'diet': round(industries, 2),  # Database field is 'diet' but represents 'industries'
        'waste': round(waste, 2),
        'total_co2': round(total_co2, 2),
        'category': category,
        'city_name': city_name,
        'state_name': state_name,
        'location_display': location_info.get('display', ''),
        'emission_factor': electricity_factor,
        'data_sources': {
            'electricity': f'Accurate state/country factor: {state_name or country_name}',
            'transport': 'EPA/IPCC emission factors',
            'industries': 'EPA industrial sector data',
            'waste': 'EPA WARM Model',
            'air_quality': air_quality['source']
        }
    }

# ======================================================================================
# ECO-EVENTS & WORKSHOPS GENERATION (Based on footprint level)
# ======================================================================================

def generate_eco_events(category):
    """Generate realistic eco-events and workshops based on footprint level"""
    
    events_low = [
        {"name": "Green Living Workshop", "type": "Workshop", "description": "Learn advanced composting and zero-waste living techniques", "location": "View on Map"},
        {"name": "Community Tree Planting", "type": "Event", "description": "Join neighbors to plant native trees in local parks", "location": "View on Map"},
        {"name": "Solar Panel Information Session", "type": "Workshop", "description": "Explore residential solar energy options and incentives", "location": "View on Map"},
        {"name": "Eco-Friendly Cooking Class", "type": "Workshop", "description": "Sustainable cooking with local, seasonal ingredients", "location": "View on Map"},
        {"name": "Climate Action Meetup", "type": "Event", "description": "Connect with local environmental advocates", "location": "View on Map"}
    ]
    
    events_medium = [
        {"name": "Carbon Footprint Reduction Workshop", "type": "Workshop", "description": "Practical strategies to cut your emissions by 30%", "location": "View on Map"},
        {"name": "Public Transit Tour", "type": "Event", "description": "Discover efficient public transport routes in your area", "location": "View on Map"},
        {"name": "Energy Audit Training", "type": "Workshop", "description": "Learn to conduct home energy audits and save money", "location": "View on Map"},
        {"name": "Recycling & Composting Fair", "type": "Event", "description": "Get free compost bins and recycling tips", "location": "View on Map"},
        {"name": "Green Commute Challenge", "type": "Event", "description": "30-day challenge to reduce transport emissions", "location": "View on Map"},
        {"name": "Sustainable Home Improvement", "type": "Workshop", "description": "Eco-friendly renovations and weatherization techniques", "location": "View on Map"}
    ]
    
    events_high = [
        {"name": "Urgent Climate Action Workshop", "type": "Workshop", "description": "Immediate steps to drastically reduce your carbon footprint", "location": "View on Map"},
        {"name": "Energy Efficiency Retrofit Program", "type": "Workshop", "description": "Home insulation, LED upgrades, and smart thermostats", "location": "View on Map"},
        {"name": "EV & Hybrid Vehicle Expo", "type": "Event", "description": "Test drive electric vehicles and learn about incentives", "location": "View on Map"},
        {"name": "Zero-Waste Living Bootcamp", "type": "Workshop", "description": "Intensive 3-day program to eliminate household waste", "location": "View on Map"},
        {"name": "Renewable Energy Fair", "type": "Event", "description": "Solar, wind, and geothermal solutions for homes", "location": "View on Map"},
        {"name": "Carbon Offset Programs Info", "type": "Workshop", "description": "Invest in verified carbon offset projects", "location": "View on Map"},
        {"name": "Green Building Certification", "type": "Workshop", "description": "LEED and green building standards for your property", "location": "View on Map"}
    ]
    
    if category == 'low':
        return random.sample(events_low, min(3, len(events_low)))
    elif category == 'medium':
        return random.sample(events_medium, min(4, len(events_medium)))
    else:  # high
        return random.sample(events_high, min(5, len(events_high)))

# ======================================================================================
# ROUTES
# ======================================================================================

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/profile')
def profile():
    user_id = get_default_user()
    conn = sqlite3.connect('eco_twin.db')
    c = conn.cursor()
    
    # Get user stats
    c.execute("SELECT * FROM user_stats WHERE user_id = ?", (user_id,))
    stats = c.fetchone()
    
    # Get calculation history
    c.execute("""SELECT total_co2, category, calculated_at, city_name 
                 FROM calculations 
                 WHERE user_id = ? 
                 ORDER BY calculated_at DESC 
                 LIMIT 10""", (user_id,))
    history = c.fetchall()
    
    conn.close()
    
    return render_template('profile.html', stats=stats, history=history)

@app.route('/suggestions')
def suggestions():
    # Get category from query parameter or use latest calculation
    category = request.args.get('category', None)
    
    if not category:
        # Get user's latest calculation category
        user_id = get_default_user()
        conn = sqlite3.connect('eco_twin.db')
        c = conn.cursor()
        c.execute("SELECT category FROM calculations WHERE user_id = ? ORDER BY calculated_at DESC LIMIT 1", (user_id,))
        result = c.fetchone()
        conn.close()
        
        if result:
            category = result[0]
        else:
            category = 'medium'  # Default if no calculations yet
    
    return render_template('suggestions.html', category=category)

# ======================================================================================
# API ENDPOINTS
# ======================================================================================

@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    try:
        data = request.json
        result = calculate_emissions(data)
        
        # Save to database
        user_id = get_default_user()
        conn = sqlite3.connect('eco_twin.db')
        c = conn.cursor()
        
        # Get current tree stage and level
        c.execute("SELECT tree_level, current_tree_stage FROM user_stats WHERE user_id = ?", (user_id,))
        stats_row = c.fetchone()
        current_tree_level = stats_row[0] if stats_row else 1
        current_tree_stage = stats_row[1] if stats_row and len(stats_row) > 1 and stats_row[1] else 1
        
        # Insert the new calculation
        c.execute("""INSERT INTO calculations 
                      (user_id, electricity, transport, diet, waste, total_co2, category, region, input_mode, latitude, longitude, city_name, state_name)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                  (user_id, result['electricity'], result['transport'], result['diet'], 
                   result['waste'], result['total_co2'], result['category'], 
                   result['state_name'], data.get('input_mode', 'question'),
                   data.get('lat', 0), data.get('lon', 0), result['city_name'], result['state_name']))
        
        # Update user stats
        c.execute("UPDATE user_stats SET total_calculations = total_calculations + 1, total_points = total_points + 10 WHERE user_id = ?", (user_id,))
        
        # Tree Stage Progression Logic based on emissions category
        # LOW emissions = grow to next stage
        # HIGH emissions = shrink down one stage  
        # MEDIUM emissions = no change
        category = result['category']
        new_tree_stage = current_tree_stage
        new_tree_level = current_tree_level
        
        if category == 'low':
            if current_tree_stage < 5:
                new_tree_stage = current_tree_stage + 1
                logging.info(f"[TREE GROWTH] LOW emissions! Stage: {current_tree_stage} -> {new_tree_stage}")
            elif current_tree_stage == 5:
                new_tree_level = current_tree_level + 1
                new_tree_stage = 1
                logging.info(f"[TREE LEVEL UP] Completed all 5 stages! Level: {current_tree_level} -> {new_tree_level}, Stage reset to 1")
        elif category == 'high':
            new_tree_stage = max(current_tree_stage - 1, 1)
            if new_tree_stage < current_tree_stage:
                logging.info(f"[TREE SHRINK] HIGH emissions! Stage: {current_tree_stage} -> {new_tree_stage}")
            else:
                logging.info(f"[TREE SHRINK] Already at minimum stage 1")
        else:
            logging.info(f"[TREE STABLE] MEDIUM emissions, stage stays at {current_tree_stage}")
        
        c.execute("UPDATE user_stats SET tree_level = ?, current_tree_stage = ? WHERE user_id = ?", 
                  (new_tree_level, new_tree_stage, user_id))
        
        conn.commit()
        conn.close()
        
        return jsonify(result)
    except Exception as e:
        logging.error(f"Calculation error: {e}", exc_info=True)
        return jsonify({'error': str(e)}), 500

@app.route('/api/weather', methods=['GET'])
def api_weather():
    lat = float(request.args.get('lat', 0))
    lon = float(request.args.get('lon', 0))
    weather = fetch_weather(lat, lon)
    return jsonify(weather)

@app.route('/api/geocode', methods=['GET'])
def api_geocode():
    lat = float(request.args.get('lat', 0))
    lon = float(request.args.get('lon', 0))
    location = reverse_geocode(lat, lon)
    return jsonify(location)

@app.route('/api/eco-events', methods=['GET'])
def api_eco_events():
    """Get eco-events and workshops based on footprint category"""
    category = request.args.get('category', 'medium')
    events = generate_eco_events(category)
    return jsonify({'events': events, 'category': category})

@app.route('/api/profile-history-detailed', methods=['GET'])
def api_profile_history():
    user_id = get_default_user()
    conn = sqlite3.connect('eco_twin.db')
    c = conn.cursor()
    
    c.execute("""SELECT total_co2, category, calculated_at, city_name, electricity, transport, diet, waste
                 FROM calculations 
                 WHERE user_id = ? 
                 ORDER BY calculated_at ASC""", (user_id,))
    rows = c.fetchall()
    conn.close()
    
    history = []
    for row in rows:
        history.append({
            'co2': row[0],
            'category': row[1],
            'date': row[2],
            'city': row[3] if row[3] else 'Unknown',
            'electricity': row[4],
            'transport': row[5],
            'diet': row[6],  # Represents industries
            'waste': row[7]
        })
    
    return jsonify(history)

@app.route('/api/delete-history', methods=['POST'])
def api_delete_history():
    user_id = get_default_user()
    conn = sqlite3.connect('eco_twin.db')
    c = conn.cursor()
    c.execute("DELETE FROM calculations WHERE user_id = ?", (user_id,))
    c.execute("UPDATE user_stats SET total_calculations = 0, tree_level = 1 WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/api/daily-fact', methods=['GET'])
def api_daily_fact():
    fact = random.choice(ECO_FACTS)
    return jsonify(fact)

@app.route('/api/complete-action', methods=['POST'])
def api_complete_action():
    data = request.json
    points = data.get('points', 10)
    
    user_id = get_default_user()
    conn = sqlite3.connect('eco_twin.db')
    c = conn.cursor()
    c.execute("UPDATE user_stats SET total_points = total_points + ?, eco_twin_happiness = MIN(eco_twin_happiness + 5, 100) WHERE user_id = ?", (points, user_id))
    conn.commit()
    conn.close()
    
    return jsonify({'success': True, 'points': points})

@app.route('/api/emission-intensity', methods=['GET'])
def api_emission_intensity():
    """Get emission intensity data for display"""
    lat = float(request.args.get('lat', 0))
    lon = float(request.args.get('lon', 0))
    
    location_info = reverse_geocode(lat, lon)
    state_name = location_info.get('state', '')
    country_name = location_info.get('country', '')
    
    electricity_factor = get_electricity_factor(state_name, country_name)
    air_quality = fetch_air_quality(lat, lon)
    
    return jsonify({
        'carbon_intensity': electricity_factor,
        'intensity_source': f'State/Country: {state_name or country_name}',
        'aqi': air_quality['aqi'],
        'aqi_source': air_quality['source'],
        'location': {'lat': lat, 'lon': lon}
    })

@app.route('/api/profile/stats', methods=['GET'])
def api_profile_stats():
    """Get user statistics for profile page"""
    user_id = get_default_user()
    conn = sqlite3.connect('eco_twin.db')
    c = conn.cursor()
    
    c.execute("SELECT total_points, eco_twin_happiness, tree_level, total_calculations, current_tree_stage FROM user_stats WHERE user_id = ?", (user_id,))
    row = c.fetchone()
    conn.close()
    
    if row:
        return jsonify({
            'total_points': row[0],
            'eco_twin_happiness': row[1],
            'tree_level': row[2],
            'total_calculations': row[3],
            'current_tree_stage': row[4] if len(row) > 4 and row[4] else 1
        })
    else:
        return jsonify({
            'total_points': 0,
            'eco_twin_happiness': 50,
            'tree_level': 1,
            'total_calculations': 0,
            'current_tree_stage': 1
        })

@app.route('/api/profile/latest', methods=['GET'])
def api_profile_latest():
    """Get latest calculation for avatar rendering"""
    user_id = get_default_user()
    conn = sqlite3.connect('eco_twin.db')
    c = conn.cursor()
    
    c.execute("""SELECT total_co2, category FROM calculations 
                 WHERE user_id = ? 
                 ORDER BY calculated_at DESC LIMIT 1""", (user_id,))
    row = c.fetchone()
    conn.close()
    
    if row:
        return jsonify({
            'total_co2': row[0],
            'category': row[1]
        })
    else:
        return jsonify({
            'total_co2': 0,
            'category': 'medium'
        })

@app.route('/api/profile/history', methods=['GET'])
def api_profile_history_list():
    """Get calculation history for profile page"""
    user_id = get_default_user()
    conn = sqlite3.connect('eco_twin.db')
    c = conn.cursor()
    
    c.execute("""SELECT total_co2, category, calculated_at, city_name, input_mode
                 FROM calculations 
                 WHERE user_id = ? 
                 ORDER BY calculated_at DESC 
                 LIMIT 10""", (user_id,))
    rows = c.fetchall()
    conn.close()
    
    history = []
    for row in rows:
        history.append({
            'total_co2': row[0],
            'category': row[1],
            'calculated_at': row[2],
            'city_name': row[3] if row[3] else 'Unknown',
            'input_mode': row[4]
        })
    
    return jsonify(history)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
