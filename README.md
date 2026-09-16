<div align="center">

🌱 EcoSessionTree

Track Your Carbon. Grow Your Eco Twin. Build a Greener Future.

A full-stack sustainability web application that helps users understand their carbon footprint, monitor environmental impact, complete eco-friendly actions, and grow a virtual Eco Twin tree based on their sustainable choices.

<br>








<br>

🌍 Carbon Footprint • 📊 Analytics • 🌳 Gamification • 📍 Location • ☁️ Weather • ♻️ Sustainability

</div>

📌 Table of Contents

About the Project

Why EcoSessionTree?

Core Features

How It Works

Carbon Footprint Calculation

Eco Twin & Gamification

Application Modules

Technology Stack

System Architecture

Project Structure

Database Design

API Documentation

Installation

Configuration

Running the Application

How to Use

Environmental Classification

Caching

Location & Weather

Security

Current Limitations

Future Improvements

Contributing

License

Author

🌍 About the Project

EcoSessionTree is a sustainability-focused web application designed to make carbon-footprint tracking simple, interactive, and engaging.

Instead of presenting environmental impact as only a number, EcoSessionTree converts a user's everyday activities into an interactive sustainability experience.

The application allows users to:

⚡ Track electricity consumption

🚗 Estimate emissions from transportation

🛍️ Estimate emissions related to consumption/industries

♻️ Track waste generation

📊 View their overall carbon footprint

🌳 Grow a virtual Eco Twin

😊 Improve Eco Twin happiness

⭐ Earn eco points

📈 Review historical calculations

📅 View monthly statistics

📍 Use location information for regional calculations

🌤️ Retrieve weather and air-quality information

💡 Discover sustainability tips

🌱 Complete eco-friendly actions

📍 Explore application-provided eco events and locations

💡 The core idea

The more sustainable your lifestyle becomes, the healthier your Eco Twin becomes.

🌱 Why EcoSessionTree?

Carbon-footprint calculators often stop after displaying a result.

EcoSessionTree adds an interactive feedback loop:

Daily Lifestyle
      ↓
Carbon Footprint Calculation
      ↓
Environmental Classification
      ↓
Eco Twin Feedback
      ↓
Points + Happiness + Tree Growth
      ↓
Eco-Friendly Actions
      ↓
Improved Lifestyle
      ↓
Lower Carbon Footprint

This makes sustainability more visual, measurable, and engaging.

✨ Core Features

⚡ 1. Carbon Footprint Calculator

Users can calculate their estimated monthly CO₂ emissions using four major categories:

Category

What It Represents

⚡ Electricity

Household electricity consumption

🚗 Transport

Monthly transportation activity

🛍️ Industries / Consumption

Lifestyle and consumption impact

♻️ Waste

Monthly waste generation

The final footprint is calculated as:

Total CO₂ = Electricity CO₂ + Transport CO₂ + Industries CO₂ + Waste CO₂

📊 2. Environmental Impact Classification

The application classifies individual categories as:

🟢 LOW

🟡 MEDIUM

🔴 HIGH

The overall classification is determined by the highest-impact category.

HIGH > MEDIUM > LOW

🌳 3. Eco Twin

The Eco Twin is the central gamification element of EcoSessionTree.

It visually represents the user's sustainability journey.

Your Eco Twin has:

❤️ Happiness

⭐ Eco points

🌳 Tree stage

🌲 Tree level

📊 Sustainability history

Better environmental performance helps the tree progress.

🌱 4. Five Tree Growth Stages

Stage

Growth

1

🌱 Tiny Seedling

2

🌿 Small Sprout

3

🌳 Young Sapling

4

🌲 Growing Tree

5

🌲 Full-Grown Tree

When all five stages are completed, the tree advances to a new tree level and begins the growth cycle again.

⭐ 5. Eco Points

Users can earn points by performing sustainable activities.

Examples:

Saving calculation: +10 points

Reduce Power Plants: +15 points

Improve Transport: +20 points

😊 6. Eco Twin Happiness

Completing an eco-friendly action increases Eco Twin happiness.

Eco Action Completed
        ↓
     +5 Happiness
        ↓
Maximum = 100

Happiness is capped at 100.

📈 7. Historical Tracking

Every carbon-footprint calculation can be stored in the SQLite database.

Users can review:

Previous calculations

Total CO₂

Category

Region

Input mode

Date and time

Location information

📅 8. Monthly Statistics

The profile dashboard provides monthly statistics that can be used to understand carbon-footprint trends over time.

💡 9. Sustainability Suggestions

EcoSessionTree provides sustainability-focused suggestions and actions covering:

Energy conservation

Transportation

Waste reduction

Sustainable lifestyle choices

🌤️ 10. Weather & Air Quality

The application can retrieve weather and air-quality information using the OpenWeather API when an API key is configured.

📍 11. Location Awareness

The application can use browser geolocation to obtain coordinates.

Location information can be used for:

Regional electricity emission factors

Reverse geocoding

City/state information

Weather information

The browser requests location permission before accessing geolocation.

📚 12. Daily Eco Facts

The home page can provide sustainability-related:

🌍 Facts

💡 Tips

📊 Environmental analogies

🧮 Carbon Footprint Calculation

EcoSessionTree divides emissions into four major categories.

⚡ Electricity Emissions

Electricity CO₂
=
Monthly Electricity Consumption
×
Regional Emission Factor

Examples of configured regional factors:

Region

Factor (kg CO₂/kWh)

India

0.708

Karnataka

0.690

Maharashtra

0.720

Tamil Nadu

0.650

Kerala

0.120

Delhi

0.730

Gujarat

0.680

Uttar Pradesh

0.760

West Bengal

0.680

A global fallback factor of 0.475 kg CO₂/kWh is used when a more specific factor is unavailable.

🚗 Transportation Emissions

Transport CO₂
=
Monthly Distance
×
Transport Emission Factor

Transport Mode

kg CO₂/km

Walking

0.000

Bicycle

0.000

Public Transport

0.041

Car

0.192

Small Car

0.145

Medium Car

0.192

Large Car / SUV

0.245

Motorcycle

0.103

Electric Car

0.053

Hybrid

0.119

Train

0.041

Metro

0.031

Bus

0.089

Short-haul Flight

0.255

Long-haul Flight

0.195

🛍️ Industries / Consumption

Question Mode

Level

Estimated CO₂

Low

120 kg/month

Medium

280 kg/month

High

580 kg/month

Number Mode

Users can directly provide an estimated value in kg CO₂/month.

♻️ Waste Emissions

Waste CO₂
=
Monthly Waste
×
Waste Emission Factor

Average waste factor:

0.89 kg CO₂/kg waste

Question-based assumptions:

Waste Level

Waste / Month

Minimal

30 kg

Average

60 kg

High

100 kg

Recycling-related factors:

Recycling Level

Factor

High Recycling

0.42

Medium Recycling

0.89

Low Recycling

1.54

🌳 Eco Twin & Gamification

EcoSessionTree connects environmental performance with a virtual ecosystem.

🌱 Tree Progression

Stage 1
🌱
Tiny Seedling
     ↓
Stage 2
🌿
Small Sprout
     ↓
Stage 3
🌳
Young Sapling
     ↓
Stage 4
🌲
Growing Tree
     ↓
Stage 5
🌲
Full-Grown Tree
     ↓
New Tree Level

📉 Footprint → Tree Behavior

Environmental Result

Tree Effect

🟢 LOW

Tree progresses

🟡 MEDIUM

Tree remains at current stage

🔴 HIGH

Tree regresses

🧩 Application Modules

🏠 Home

Provides:

Project introduction

Eco Twin concept

Sustainability information

Daily eco facts

Navigation to application features

🧮 Calculator

Handles:

Electricity input

Transport input

Consumption input

Waste input

Regional calculations

CO₂ calculation

Environmental classification

Result presentation

Calculation persistence

👤 Profile

Provides:

Eco points

Eco Twin happiness

Tree level

Tree stage

Total calculations

Latest footprint

Historical calculations

Monthly statistics

💡 Suggestions

Provides:

Eco-friendly actions

Sustainability recommendations

Eco events

Application-provided locations

Action completion

🛠️ Technology Stack

Layer

Technology

Backend

Python + Flask

Frontend

HTML5 + CSS3 + Vanilla JavaScript

Templates

Jinja2

Database

SQLite

Charts

Chart.js

Maps

Leaflet.js + OpenStreetMap

HTTP/API

Requests

Configuration

python-dotenv

Weather/AQI

OpenWeather API

Geocoding

Nominatim

Location

Browser Geolocation API

🏗️ System Architecture

                         ┌──────────────────────┐
                         │      Web Browser     │
                         │ HTML / CSS / JS      │
                         └──────────┬───────────┘
                                    │
                                    │ HTTP
                                    ▼
                         ┌──────────────────────┐
                         │      Flask App       │
                         │       app.py         │
                         └──────────┬───────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                  │
                 ▼                  ▼                  ▼
        ┌────────────────┐ ┌────────────────┐ ┌─────────────────┐
        │ Carbon Engine  │ │ Eco Twin Logic │ │ External APIs   │
        │                │ │                │ │                 │
        │ Electricity    │ │ Points         │ │ OpenWeather     │
        │ Transport      │ │ Happiness      │ │ Nominatim       │
        │ Consumption    │ │ Tree Growth    │ │ OpenStreetMap   │
        │ Waste          │ │ Actions        │ │                 │
        └───────┬────────┘ └───────┬────────┘ └─────────────────┘
                │                  │
                └─────────┬────────┘
                          ▼
                 ┌──────────────────┐
                 │      SQLite      │
                 │   eco_twin.db    │
                 └──────────────────┘

📁 Project Structure

EcoSessionTree/
│
├── app.py
├── eco_twin.db
├── .gitignore
├── .replit
├── replit.md
│
├── templates/
│   ├── home.html
│   ├── calculator.html
│   ├── profile.html
│   └── suggestions.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── images/
│       ├── eco-twin-high.jpg
│       ├── eco-twin-medium.jpg
│       └── eco-twin-low.jpg
│
└── attached_assets/
    ├── app_1763512054590.py
    ├── calculator_1763512078198.html
    ├── eco-twin-high_1763512102628.jpg
    ├── eco-twin-low_1763512102629.jpg
    ├── eco-twin-medium_1763512102631.jpg
    ├── eco_twin_1763512054591.db
    ├── home_1763512078200.html
    ├── profile_1763512078201.html
    ├── style_1763512090352.css
    └── suggestions_1763512069523.html

Note: attached_assets/ contains development/source copies and supporting assets. The main application uses the files in templates/ and static/.

🗄️ Database Design

EcoSessionTree uses SQLite for persistent application data.

Database:

eco_twin.db

👤 users

Column

Type

id

INTEGER

username

TEXT

email

TEXT

created_at

TIMESTAMP

📊 calculations

Column

Type

Description

id

INTEGER

Calculation ID

user_id

INTEGER

Associated user

electricity

REAL

Electricity emissions

transport

REAL

Transport emissions

diet

REAL

Industries / consumption emissions

waste

REAL

Waste emissions

total_co2

REAL

Total emissions

category

TEXT

LOW / MEDIUM / HIGH

region

TEXT

Calculation region

input_mode

TEXT

Input method

calculated_at

TIMESTAMP

Calculation timestamp

latitude

REAL

Latitude

longitude

REAL

Longitude

city_name

TEXT

City

state_name

TEXT

State

📈 user_stats

Column

Type

user_id

INTEGER

total_points

INTEGER

eco_twin_happiness

INTEGER

tree_level

INTEGER

current_tree_stage

INTEGER

total_calculations

INTEGER

🔌 API Documentation

Endpoint

Method

Purpose

/api/calculate

POST

Calculate and store carbon footprint

/api/weather

GET

Retrieve weather information

/api/geocode

GET

Reverse geocode coordinates

/api/eco-events

GET

Retrieve eco events

/api/profile-history-detailed

GET

Retrieve detailed calculation history

/api/delete-history

POST

Delete calculation history

/api/daily-fact

GET

Retrieve daily sustainability fact

/api/complete-action

POST

Complete an eco action

/api/emission-intensity

GET

Retrieve emission-intensity information

/api/profile/stats

GET

Retrieve profile statistics

/api/profile/latest

GET

Retrieve latest calculation

/api/profile/history

GET

Retrieve profile history

/api/profile/monthly-stats

GET

Retrieve monthly statistics

⚙️ Backend Functions

Important application functions include:

init_db()
get_default_user()
get_cache_key()
get_from_cache()
set_to_cache()
reverse_geocode()
get_electricity_factor()
fetch_weather()
fetch_air_quality()
calculate_emissions()
generate_eco_events()

Main Flask route handlers include:

home()
calculator()
profile()
suggestions()

api_calculate()
api_weather()
api_geocode()
api_eco_events()
api_profile_history()
api_delete_history()
api_daily_fact()
api_complete_action()
api_emission_intensity()
api_profile_stats()
api_profile_latest()
api_profile_history_list()
api_monthly_stats()

🚀 Installation

1. Clone the Repository

git clone https://github.com/priyanshushe/EcoSessionTree.git
cd EcoSessionTree

2. Create a Virtual Environment

Windows

python -m venv .venv
.\.venv\Scripts\Activate.ps1

macOS / Linux

python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies

pip install Flask requests python-dotenv

🔐 Configuration

EcoSessionTree uses environment variables for configuration.

Required:

SESSION_SECRET

Optional:

OPENWEATHER_API_KEY

Generate a Secure Session Secret

python -c "import secrets; print(secrets.token_hex(32))"

Create a local .env file and add your actual values:

SESSION_SECRET=your-generated-secret
OPENWEATHER_API_KEY=your-openweather-key

Important: Never commit .env, API keys, passwords, or other secrets to GitHub.

Recommended .gitignore entries:

.env
*.env

▶️ Running the Application

Start the Flask application:

python app.py

Open:

http://127.0.0.1:5000

The server is configured to bind to:

0.0.0.0:5000

🧭 How to Use

1. Open the Application

Visit the home page.

2. Open the Calculator

Navigate to:

/calculator

3. Enter Lifestyle Information

Provide information about:

Electricity consumption

Transportation

Consumption/lifestyle

Waste

4. Calculate Your Footprint

The application calculates emissions for each category and combines them into an overall estimated footprint.

5. Review Your Eco Twin

Your result influences:

🌳 Tree stage

⭐ Eco points

❤️ Happiness

📊 Profile statistics

6. Take Eco Actions

Visit:

/suggestions

Complete sustainable actions to earn points and improve your Eco Twin.

7. Track Your Progress

Visit:

/profile

to view your latest footprint, calculation history, monthly statistics, Eco points, tree progress, and Eco Twin happiness.

🌤️ Location & Weather Integration

The application can use browser-based geolocation.

Browser
   ↓
Location Permission
   ↓
Latitude + Longitude
   ↓
Reverse Geocoding
   ↓
City + State
   ↓
Regional Emission Factor

Weather information follows a similar flow:

User Location
      ↓
Coordinates
      ↓
OpenWeather API
      ↓
Weather / AQI Information
      ↓
Application UI

The user must grant browser location permission for location-based functionality.

⚡ API Caching

EcoSessionTree uses an in-memory caching mechanism for external API data.

Cached information can remain available for approximately:

5 minutes

Helper functions include:

get_cache_key()
get_from_cache()
set_to_cache()

This reduces unnecessary external requests and improves responsiveness.

🛡️ Security

EcoSessionTree follows several basic security practices.

Environment Secrets

Sensitive configuration values are kept outside the source code.

Git Ignore

Environment files should be excluded using:

.env
*.env

Location Permission

Location access depends on explicit browser permission.

Production Security

Before public deployment, additional protections should be implemented:

Production-grade authentication

Authorization

CSRF protection

Input validation

Rate limiting

Secure cookies

HTTPS

Production WSGI server

Centralized secret management

Stronger API error handling

Production database configuration

⚠️ Current Limitations

Authentication

The current implementation uses a lightweight/default-user approach rather than a complete production authentication system.

Eco Locations

Nearby eco-friendly locations are represented using application-defined data rather than a live places-discovery service.

Eco Events

Eco events are application-defined events rather than a continuously synchronized external event database.

Database

SQLite is suitable for development and smaller deployments but may not be ideal for a large production workload.

Flask Debug Mode

The current development configuration uses Flask debug mode. For production deployment, debug mode should be disabled.

🔮 Future Improvements

🔐 Authentication

User registration

Login/logout

Password hashing

Email verification

OAuth authentication

User-specific dashboards

📊 Advanced Analytics

Weekly trends

Yearly trends

Category comparisons

Carbon-reduction percentages

Personal sustainability goals

Interactive dashboards

🤖 AI-Based Recommendations

An AI recommendation engine could analyze a user's footprint and generate personalized suggestions.

High Transport Emissions
        ↓
Analyze Transport Pattern
        ↓
Personalized Recommendations
        ↓
Public Transport
Carpooling
Cycling
Walking

🌍 Real-Time Eco Locations

Integration with live location/places APIs could provide:

Recycling centers

EV charging stations

Public transport

Organic stores

Sustainable restaurants

Green spaces

🏆 Leaderboards

Users could compare sustainability progress through:

Individual rankings

College rankings

Community rankings

Monthly challenges

🎯 Sustainability Challenges

Examples:

🚲 Car-Free Week

💡 Energy Saving Challenge

♻️ Zero-Waste Week

🌳 Tree Plantation Challenge

🚆 Public Transport Challenge

📱 Mobile Application

The Flask backend could be reused as an API backend for Android, iOS, React Native, or Flutter applications.

☁️ Production Deployment

Potential production architecture:

Client
  ↓
HTTPS
  ↓
Nginx
  ↓
Gunicorn / WSGI
  ↓
Flask
  ↓
PostgreSQL

🧪 Example User Journey

                🌱 EcoSessionTree
                       │
                       ▼
              Enter Lifestyle Data
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
     Electricity    Transport    Waste
          │            │            │
          └────────────┼────────────┘
                       ▼
                CO₂ Calculation
                       │
                       ▼
             Environmental Result
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
        Points      Happiness      Tree
          │            │            │
          └────────────┼────────────┘
                       ▼
                 Eco Actions
                       │
                       ▼
               Better Habits
                       │
                       ▼
                🌳 Growing Tree

💡 Design Philosophy

EcoSessionTree is built around three principles:

1. Awareness

Users should understand how everyday activities contribute to their estimated carbon footprint.

2. Feedback

Users should immediately see the effect of their environmental choices.

3. Motivation

Sustainability should feel like a continuous journey rather than a one-time calculation.

The application therefore combines:

Carbon Tracking + Analytics + Gamification + Eco Actions

📌 Key Project Highlights

<div align="center">

🌍 Sustainability

📊 Analytics

🌳 Gamification

Carbon footprint

Historical data

Eco Twin

Regional factors

Monthly statistics

Tree growth

Waste tracking

Profile dashboard

Happiness

Transport tracking

Category analysis

Eco points

</div>

📚 Learning Outcomes

This project demonstrates practical implementation of:

Flask web development

REST-style API endpoints

SQLite database integration

CRUD operations

Jinja2 templating

HTML/CSS/JavaScript integration

External API integration

Browser Geolocation API

Reverse geocoding

Data visualization

Caching

Environmental calculations

Gamification logic

Environment variable management

Git/GitHub project management

🤝 Contributing

Contributions and improvements are welcome.

1. Fork the repository

Create your own fork of the project on GitHub.

2. Create a feature branch

git checkout -b feature/your-feature

3. Make your changes

Implement and test your feature.

4. Commit your changes

git add .
git commit -m "Add new sustainability feature"

5. Push the branch

git push origin feature/your-feature

6. Open a Pull Request

Describe what changed, why it was changed, and how it was tested.

📜 License

No explicit open-source license is currently included in the repository.

Until a license is added, the project should be treated as all rights reserved.

👨‍💻 Author

<div align="center">

Priyanshu Shekhar

Final Year BE (CSE) Student

Developer • DSA Enthusiast • Frontend Developer • Cloud Learner

<br>





</div>

<div align="center">

🌱 Track your footprint. Improve your habits. Grow your Eco Twin.

EcoSessionTree — Making sustainability measurable, interactive, and engaging.

<br>

⭐ If you find this project interesting, consider giving the repository a star! ⭐

</div>
