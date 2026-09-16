#🌍 Eco Twin

A location-aware carbon footprint calculator that turns everyday environmental data into an interactive personal Eco Twin experience.

Eco Twin is a Flask-based web application for estimating monthly CO₂ emissions across electricity, transportation, industrial/consumption impact, and waste. It combines GPS-based regional information, configurable emission factors, visual analytics, calculation history, and gamification to make carbon tracking more engaging.

The application provides two ways to calculate a footprint:

Question Mode – answer simple qualitative questions and let the application use predefined monthly activity estimates.

Number Mode – enter numerical monthly values for more direct control over the calculation.

After each calculation, Eco Twin stores the result locally in SQLite, awards points, updates the user's tree progression, and makes the result available on the profile dashboard.

✨ Features

🌱 Carbon Footprint Calculator

Calculates estimated monthly CO₂ emissions in kg CO₂/month.

Also displays the equivalent annual value in tonnes CO₂/year.

Breaks emissions into four categories:

⚡ Electricity

🚗 Transport

🏭 Industries / consumption impact

🗑️ Waste

Classifies the result as Low, Medium, or High.

Uses the highest category among the four sections as the overall footprint category.

❓ Question Mode

Designed for users who do not know their exact monthly figures.

The application converts simple choices into predefined activity estimates:

Category

Low / Minimal

Medium / Average

High

Electricity

100 kWh/month

300 kWh/month

600 kWh/month

Transport

0 km/month

Depends on selected transport

Depends on selected transport

Industries

120 kg CO₂/month

280 kg CO₂/month

580 kg CO₂/month

Waste

30 kg/month

60 kg/month

100 kg/month

For transport, the qualitative choices include walking/biking, public transit, car, and SUV.

🔢 Number Mode

Allows users to directly enter:

Electricity consumption in kWh/month

Transport distance in km/month

Industrial/consumption emissions in kg CO₂/month

Waste generated in kg/month

📍 GPS-Based Location Awareness

The calculator uses the browser's Geolocation API to obtain the user's coordinates.

Those coordinates are then used to:

Reverse-geocode the location into a city/state/country.

Select a regional electricity emission factor.

Display the user's location on an interactive map.

Retrieve optional weather information.

Retrieve air-quality information.

Location data is required by the calculator interface because the electricity calculation can vary by region.

🗺️ Interactive Maps

The calculator uses Leaflet.js and OpenStreetMap tiles to display the detected location.

The Suggestions page also provides category-based eco-friendly location cards with Google Maps directions generated from the user's current coordinates.

The nearby eco-friendly locations shown by the Suggestions page are application-defined example locations relative to the user's coordinates; they are not retrieved from a live places database.

🌤️ Weather & Air Quality

When an OPENWEATHER_API_KEY is configured, Eco Twin can display:

Current temperature

Weather description

Humidity

Wind speed

Air Quality Index (AQI)

The application continues to work without the API key. In that case it uses fallback values for weather/AQI display.

📊 Profile Dashboard

The Profile page provides:

Total points

Eco Twin happiness score

Total number of calculations

Current tree stage

Current tree level

Latest footprint category

Monthly emissions summary

Emissions by category

Carbon footprint progress chart

Recent calculation history

Chart.js is used to visualize historical footprint changes.

🌳 Gamification

Eco Twin includes a lightweight progression system:

Every saved calculation awards 10 points.

Completing a suggested eco-action awards additional points.

Eco Twin happiness increases when an action is completed, up to 100.

Low-emission calculations grow the tree to the next stage.

High-emission calculations can reduce the tree stage.

Medium-emission calculations leave the current tree stage unchanged.

Completing all five tree stages increases the tree level and resets the stage to 1.

Tree stages range from 1 to 5, while tree levels are displayed from 1 to 100 in the profile UI.

💡 Eco-Friendly Suggestions

The Suggestions page contains recommendations for:

Electricity and energy usage

Transportation

Industries / consumption

Waste management

Users can filter suggestions using tabs and mark actions as completed to earn points.

🌿 Eco Events & Workshops

The application includes curated sustainability event/workshop cards and also exposes an API that generates category-specific event suggestions.

The event content in the current project is static application content, not a live event-search service.

📈 Calculation History

Each calculation is stored in SQLite with information such as:

CO₂ total

Category

Calculation timestamp

Location

Latitude/longitude

Electricity emissions

Transport emissions

Industrial/consumption emissions

Waste emissions

Input mode

The profile dashboard displays the latest 10 calculations.

💾 Calculator State Persistence

The calculator stores its current location/result state in browser sessionStorage, allowing the page to restore the latest calculator state during the same browser session.

🧮 How the Calculation Works

Eco Twin calculates:

Total CO₂ = Electricity + Transport + Industries + Waste

Electricity

Electricity CO₂ = Monthly kWh × Regional Electricity Factor

The application contains regional electricity factors for India, Indian states/union territories, and a global fallback factor.

If a matching state/country factor cannot be found, the code uses:

0.475 kg CO₂/kWh

Transport

Transport CO₂ = Monthly Distance × Transport Emission Factor

The application contains predefined factors for walking, bicycle, public transport, cars, SUVs, motorcycles, electric cars, hybrids, trains, metros, buses, and short-/long-haul flights.

Question Mode uses predefined daily-distance assumptions for its supported choices, while Number Mode currently applies the application's car factor to the supplied monthly distance.

Industries / Consumption

Question Mode uses predefined monthly estimates:

Low    = 120 kg CO₂/month
Medium = 280 kg CO₂/month
High   = 580 kg CO₂/month

Number Mode accepts the industrial/consumption CO₂ value directly.

Waste

Waste CO₂ = Monthly Waste × Waste Emission Factor

The current average waste factor is:

0.89 kg CO₂ per kg of waste

🏷️ Footprint Classification

Each emission category has its own thresholds.

Category

Low

Medium

High

Electricity

< 150 kg/month

150–<300 kg/month

≥ 300 kg/month

Transport

< 80 kg/month

80–<150 kg/month

≥ 150 kg/month

Industries

< 150 kg/month

150–<300 kg/month

≥ 300 kg/month

Waste

< 40 kg/month

40–<70 kg/month

≥ 70 kg/month

The overall footprint uses the highest-severity category among the four sections:

High > Medium > Low

This category controls the Eco Twin visual state and tree progression.

📍 Location & External Services

OpenStreetMap / Nominatim

Eco Twin uses Nominatim reverse geocoding to convert latitude/longitude into readable location information.

It also uses OpenStreetMap tiles through Leaflet for map visualization.

OpenWeather

OpenWeather is optional and is used for current weather and air-quality display.

Without an API key:

Weather displays a fallback/unavailable state.

AQI falls back to a moderate AQI value for display.

Carbon-footprint calculation itself still works.

Caching

External location/weather/AQI responses are cached in memory for 5 minutes to reduce repeated external requests.

🏗️ Architecture

Eco Twin follows a lightweight monolithic Flask architecture.

┌───────────────────────────────────────────────┐
│                 Web Browser                   │
│                                               │
│  HTML + Jinja2 + CSS + Vanilla JavaScript     │
│  Leaflet.js + Chart.js + Geolocation API      │
└───────────────────────┬───────────────────────┘
                        │ HTTP / JSON
                        ▼
┌───────────────────────────────────────────────┐
│                  Flask App                    │
│                    app.py                     │
│                                               │
│  Page Routes                                  │
│  REST-style API Routes                        │
│  Emission Calculation Engine                  │
│  Location / Weather / AQI Integration         │
│  Caching                                      │
│  Gamification Logic                           │
└───────────────┬───────────────────┬───────────┘
                │                   │
                ▼                   ▼
        ┌───────────────┐   ┌──────────────────┐
        │   SQLite DB   │   │ External Services │
        │ eco_twin.db   │   │ Nominatim         │
        │               │   │ OpenWeather       │
        └───────────────┘   └──────────────────┘

Frontend

HTML5

Jinja2 templates

CSS3

Vanilla JavaScript

Leaflet.js 1.9.4

Chart.js

Browser Geolocation API

Browser sessionStorage

Backend

Python 3.11

Flask

SQLite3

Requests

python-dotenv

Python logging

Data Storage

SQLite is used as a zero-configuration local relational database.

The application automatically creates/updates the required tables when it starts.

📁 Project Structure

EcoSessionTree/
│
├── app.py                         # Flask application, APIs, calculations and database logic
├── eco_twin.db                    # SQLite database used by the application
├── replit.md                      # Replit/project architecture notes
├── .replit                        # Replit runtime and workflow configuration
├── .gitignore                     # Ignores environment files
│
├── templates/
│   ├── home.html                  # Landing page and daily eco-fact
│   ├── calculator.html            # Carbon footprint calculator
│   ├── profile.html               # Profile, statistics, chart and history
│   └── suggestions.html           # Recommendations, actions, events and maps
│
├── static/
│   ├── css/
│   │   └── style.css              # Main application stylesheet
│   └── images/
│       ├── eco-twin-high.jpg       # High-footprint Eco Twin state
│       ├── eco-twin-medium.jpg     # Medium-footprint Eco Twin state
│       └── eco-twin-low.jpg        # Low-footprint Eco Twin state
│
└── attached_assets/               # Project/source assets retained from the development environment

The attached_assets/ directory contains development copies of application files/assets. The application itself serves the files from templates/ and static/.

🌐 Application Pages

Route

Purpose

/

Eco Twin landing page with daily eco-fact

/calculator

Location-aware carbon footprint calculator

/profile

User statistics, tree progression, charts and history

/suggestions

Eco-friendly recommendations, actions, events and locations

🔌 API Endpoints

Endpoint

Method

Purpose

/api/calculate

POST

Calculates emissions and stores the result

/api/weather

GET

Retrieves current weather data

/api/geocode

GET

Reverse-geocodes coordinates

/api/eco-events

GET

Generates category-based eco-events/workshops

/api/profile-history-detailed

GET

Returns detailed calculation history

/api/delete-history

POST

Deletes the user's calculation history and resets core progress

/api/daily-fact

GET

Returns a random eco-fact, action tip and analogy

/api/complete-action

POST

Awards points and increases Eco Twin happiness

/api/emission-intensity

GET

Returns regional carbon intensity and AQI information

/api/profile/stats

GET

Returns profile statistics

/api/profile/latest

GET

Returns the latest footprint result

/api/profile/history

GET

Returns the latest 10 calculations

/api/profile/monthly-stats

GET

Returns current-month aggregated emissions

Example Calculation Request

{
  "lat": 12.9716,
  "lon": 77.5946,
  "input_mode": "question",
  "electricity_q": "medium",
  "transport_q": "car",
  "industries_q": "medium",
  "waste_q": "average",
  "individual_sections": null
}

Example Number Mode Request

{
  "lat": 12.9716,
  "lon": 77.5946,
  "input_mode": "number",
  "electricity_n": 300,
  "transport_n": 600,
  "industries_n": 280,
  "waste_n": 60,
  "individual_sections": null
}

🗄️ Database Schema

users

Stores the application user record.

Column

Description

id

Primary key

username

Unique username

email

User email

created_at

Account creation timestamp

calculations

Stores carbon-footprint calculation history.

Column

Description

id

Primary key

user_id

Associated user

electricity

Electricity CO₂ emissions

transport

Transport CO₂ emissions

diet

Database field used to store industrial/consumption emissions

waste

Waste CO₂ emissions

total_co2

Total calculated CO₂

category

Low, Medium or High

region

Region/state associated with calculation

input_mode

Question or Number mode

calculated_at

Calculation timestamp

latitude

GPS latitude

longitude

GPS longitude

city_name

Reverse-geocoded city/locality

state_name

Reverse-geocoded state

user_stats

Stores gamification progress.

Column

Description

user_id

Primary/foreign key to user

total_points

Accumulated points

eco_twin_happiness

Happiness score, capped at 100

tree_level

Current tree level

current_tree_stage

Current stage from 1 to 5

total_calculations

Number of saved calculations

🔐 Environment Configuration

Eco Twin reads environment variables using python-dotenv.

Required

SESSION_SECRET

The application exits at startup if SESSION_SECRET is not set because it is used as the Flask session signing key.

Generate a strong value locally with Python:

python -c "import secrets; print(secrets.token_hex(32))"

Set the generated value in your local environment or .env file.

Optional

OPENWEATHER_API_KEY

If this variable is not configured, the application still runs and uses fallback weather/AQI display values.

Security

Never commit .env or other environment files to Git. The repository's .gitignore is configured to ignore:

.env
*.env

If a real API key or secret has ever been committed, removing the file is not sufficient. The credential should be revoked/rotated and the Git history cleaned before publishing the repository.

🚀 Local Setup

1. Clone the repository

git clone https://github.com/priyanshushe/EcoSessionTree.git
cd EcoSessionTree

2. Create a virtual environment

Windows PowerShell

python -m venv .venv
.\.venv\Scripts\Activate.ps1

macOS / Linux

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

The current project does not include a requirements.txt, so install the Python packages used by app.py directly:

pip install Flask requests python-dotenv

4. Configure the required session secret

PowerShell:

$env:SESSION_SECRET = python -c "import secrets; print(secrets.token_hex(32))"

For a persistent local configuration, create a .env file and place the generated SESSION_SECRET value there. Keep that file out of Git.

5. Optional: configure OpenWeather

Add OPENWEATHER_API_KEY to your local environment if you want live weather and AQI information.

6. Run the application

python app.py

The Flask development server listens on:

http://127.0.0.1:5000

The application is configured to bind to 0.0.0.0:5000, which also makes it suitable for environments such as Replit that expose the local port externally.

▶️ Running on Replit

The repository includes a .replit configuration for Python 3.11.

The configured workflow starts the application with:

python app.py

and exposes the Flask application through port 5000.

Before running the project on Replit, configure SESSION_SECRET in the Replit Secrets/environment configuration. OPENWEATHER_API_KEY can also be added if live weather/AQI data is required.

🔄 Typical User Flow

Open Eco Twin
      │
      ▼
Visit Calculator
      │
      ▼
Allow Browser Location
      │
      ├──► Reverse Geocoding
      ├──► Regional Carbon Intensity
      ├──► Weather / AQI
      └──► Map Display
      │
      ▼
Choose Question Mode or Number Mode
      │
      ▼
Select/Enter Activity Data
      │
      ▼
Calculate Footprint
      │
      ▼
CO₂ Total + Category + Breakdown
      │
      ▼
Save Calculation to SQLite
      │
      ▼
Update Points + Tree + Happiness
      │
      ├──► Profile Dashboard
      └──► Personalized Suggestions

🎮 Gamification Logic

When a calculation is saved:

The user receives 10 points.

The calculation category is evaluated.

Low emissions advance the tree stage.

When stage 5 is completed, the tree level increases and the stage returns to 1.

Medium emissions keep the tree at its current stage.

High emissions reduce the tree stage by one, but never below stage 1.

When an eco-action is completed:

The supplied action points are added to the total.

Eco Twin happiness increases by 5.

Happiness is capped at 100.

Current suggestion action rewards include:

Action area

Points

Power Plants / Electricity

+15

Transport

+20

Industries

+25

Waste

+15

🧠 Design Decisions

Flask + Server-Side Templates

Flask and Jinja2 keep the application lightweight while still allowing dynamic pages and JSON APIs.

Vanilla JavaScript

Client-side functionality is implemented without a frontend framework, reducing setup complexity while providing interactive maps, charts, mode switching, state persistence, and asynchronous API calls.

SQLite

SQLite provides simple, zero-configuration persistence for a small/local application without requiring a separate database server.

In-Memory Caching

A simple Python dictionary with a five-minute TTL reduces repeated requests to external services. This is appropriate for a small deployment but would normally be replaced with a shared cache such as Redis for horizontally scaled production deployments.

⚠️ Important Implementation Notes

The application is an estimation tool, not a certified carbon-accounting system.

Question Mode relies on predefined activity assumptions rather than user-specific measurements.

Emission factors are hard-coded in app.py.

The electricity factor is location-sensitive, while the current Number Mode transport calculation uses the application's car emission factor for the supplied monthly distance.

The calculations.diet database column is retained from an earlier schema but currently stores industrial/consumption emissions.

The current application uses a single default_user record rather than a full registration/login system.

eco_twin.db is local SQLite state and should generally not be treated as production database infrastructure.

The event cards and nearby eco-location cards are application-defined content rather than live discovery from an events/places provider.

The Flask server is configured with debug=True in app.py; disable debug mode before production deployment.

🔒 Privacy & Security Considerations

Eco Twin uses browser geolocation only when the user grants permission through the browser.

The application stores calculation-related location coordinates and derived city/state information in its local SQLite database. The current project does not implement a traditional multi-user authentication system.

For deployment:

Keep SESSION_SECRET private.

Keep OPENWEATHER_API_KEY private.

Never commit .env files.

Rotate any credential that has previously been exposed.

Disable Flask debug mode.

Use HTTPS when deployed publicly.

Apply rate limiting and stronger validation if the APIs are exposed to untrusted users.

Consider PostgreSQL and a shared cache for multi-user production deployments.

🛠️ Technology Stack

Layer

Technology

Language

Python 3.11

Backend

Flask

Templating

Jinja2

Database

SQLite3

HTTP Client

Requests

Environment Management

python-dotenv

Frontend

HTML5, CSS3, Vanilla JavaScript

Maps

Leaflet.js 1.9.4 + OpenStreetMap

Charts

Chart.js

Location

Browser Geolocation API

Reverse Geocoding

OpenStreetMap Nominatim

Weather / AQI

OpenWeather API

Deployment Configuration

Replit

📜 License

No license file is currently included in the project repository. The project should therefore be treated as all rights reserved unless a license is added by the project owner.

👨‍💻 Project

Eco Twin — Carbon Footprint Calculator

Repository: https://github.com/priyanshushe/EcoSessionTree

Built with Python, Flask, SQLite, JavaScript, Leaflet, Chart.js, OpenStreetMap, and optional OpenWeather integration.
