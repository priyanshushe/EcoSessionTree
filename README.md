<div align="center">

🌱 EcoSessionTree

Eco Twin — Carbon Footprint Calculator & Sustainability Tracker

Measure your environmental impact, understand where your emissions come from, and grow your virtual Eco Tree through sustainable actions.

<br>








</div>

📖 About the Project

EcoSessionTree is a sustainability-focused full-stack web application presented in the interface as Eco Twin.

The application helps users estimate their monthly carbon footprint from everyday activities and understand the major sources contributing to their emissions.

The system calculates emissions across four categories:

⚡ Electricity

🚗 Transport

🏭 Industries / Consumption

🗑️ Waste

After calculating a footprint, users receive:

Total monthly CO₂ emissions

Estimated annual CO₂ emissions

Category-wise emission breakdown

Low / Medium / High footprint classification

Regional electricity emission information

Location, weather and air-quality information

Personalized sustainability suggestions

Eco-actions and points

Eco Twin progression

Tree growth and level progression

Calculation history and visual analytics

The project combines web development, APIs, geolocation, databases, data visualization and gamification around an environmental sustainability use case.

🎯 Objectives

The main objectives of EcoSessionTree are to:

Make carbon-footprint estimation simple for everyday users.

Allow users to calculate emissions without requiring detailed technical knowledge.

Provide a numerical input mode for users who know their consumption.

Break down emissions into understandable categories.

Use location information to improve electricity-emission estimates.

Provide environmental context through weather and AQI information.

Encourage sustainable behaviour using points and Eco Tree progression.

Store historical calculations for personal progress tracking.

Provide actionable suggestions based on footprint categories.

✨ Features

🌍 Carbon Footprint Calculator

The calculator estimates monthly emissions in kg CO₂/month and converts the result into an annual tonnes CO₂/year value.

It provides a breakdown for:

Category

Measurement

⚡ Electricity

kg CO₂/month

🚗 Transport

kg CO₂/month

🏭 Industries / Consumption

kg CO₂/month

🗑️ Waste

kg CO₂/month

❓ Question Mode

Question Mode is designed for users who do not know their exact monthly consumption.

The user answers simple questions about:

Electricity usage

Transportation

Industries / consumption

Waste

The application maps these answers to predefined activity assumptions and emission factors.

🔢 Number Mode

Number Mode allows users to provide numerical monthly values.

Supported inputs:

Electricity → kWh/month

Transport → km/month

Industries → kg CO₂/month

Waste → kg/month

☑️ Individual Section Calculation

The calculator also supports selecting individual sections.

Users can choose to calculate:

Electricity only

Transport only

Industries only

Waste only

This makes it possible to analyze a specific emission source instead of calculating every category together.

📍 GPS Location

The browser's Geolocation API is used to obtain:

Latitude

Longitude

The coordinates are then used by the backend for environmental and location-related features.

🗺️ Interactive Map

The calculator displays the detected location using:

Leaflet.js

OpenStreetMap

📌 Reverse Geocoding

Latitude and longitude are converted into location information using the Nominatim reverse-geocoding service.

The application can obtain information such as:

City

State

Country

Display location

⚡ Regional Electricity Emission Factors

The application contains electricity emission factors for:

India

Indian states

Indian union territories

A regional factor is selected when the detected state is available. A country/global fallback is used when a more specific factor cannot be determined.

🌤️ Weather Information

When the OpenWeather API key is configured, the application can display:

Temperature

Weather condition

Humidity

Wind speed

🌫️ Air Quality

The application can retrieve AQI information from OpenWeather when the API key is configured.

💡 Eco Suggestions

The Suggestions page provides sustainability recommendations for:

⚡ Power Plants / Electricity

🚗 Transport

🏭 Industries

🗑️ Waste Management

Suggestions are grouped according to footprint level:

Low

Medium

High

⭐ Eco Actions

Users can mark sustainability actions as completed.

Completing an action:

Adds points

Increases Eco Twin happiness

Provides feedback to the user

🌳 Eco Tree Progression

The application contains a five-stage virtual tree.

A user's footprint affects the tree:

LOW      → Tree grows
MEDIUM   → Tree remains stable
HIGH     → Tree shrinks

Completing all five stages increases the tree level and resets the stage to one.

🏆 Points & Happiness

The application maintains:

Total points

Eco Twin happiness

Tree level

Current tree stage

Total calculations

Saving a calculation awards 10 points.

Completing an eco-action awards the points associated with that action and increases happiness by 5, capped at 100.

📊 Profile Dashboard

The Profile page provides:

Eco Twin state

Tree stage

Tree level

Happiness

Total points

Total calculations

Current-month footprint

Category-wise monthly emissions

Historical footprint chart

Calculation history

📈 Calculation History

The application stores historical calculations with:

Total CO₂

Category

Date/time

City

State

Latitude

Longitude

Input mode

Electricity emissions

Transport emissions

Industries emissions

Waste emissions

🌿 Eco Events & Workshops

The application can generate category-based sustainability events and workshops such as:

Green Living Workshop

Community Tree Planting

Solar Panel Information Session

Carbon Footprint Reduction Workshop

Public Transit Tour

Energy Audit Training

Recycling & Composting Fair

Green Commute Challenge

Renewable Energy Fair

Zero-Waste Living Bootcamp

EV & Hybrid Vehicle Expo

The events are generated from application-defined content and are not retrieved from a live event database.

💚 Daily Eco Facts

The home page can display randomly selected sustainability facts containing:

Eco fact

Action tip

Real-world analogy

🧮 Carbon Calculation Methodology

The application's overall formula is:

Total CO₂ =
Electricity CO₂
+ Transport CO₂
+ Industries CO₂
+ Waste CO₂

All results are represented as estimated monthly emissions.

⚡ Electricity Calculation

Electricity CO₂ =
Monthly Electricity Consumption × Electricity Emission Factor

The application includes regional electricity factors.

Examples from the configured dataset include:

Region

kg CO₂/kWh

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

🚗 Transport Calculation

Transport CO₂ =
Monthly Distance × Transport Emission Factor

Configured transport factors include:

Transport

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

In Question Mode, predefined daily-distance assumptions are used for selected transport choices.

In Number Mode, the entered monthly distance is multiplied by the application's configured car factor of 0.192 kg CO₂/km.

🏭 Industries / Consumption

Question Mode uses:

Level

Monthly CO₂

Low

120 kg

Medium

280 kg

High

580 kg

In Number Mode, the entered industries value is treated directly as monthly kg CO₂.

Implementation note: the SQLite column is named diet for historical/schema compatibility, but the application uses this field to store Industries / Consumption emissions.

🗑️ Waste Calculation

Waste CO₂ =
Monthly Waste × Waste Emission Factor

The configured average waste factor is:

0.89 kg CO₂ / kg waste

Question Mode uses these monthly waste assumptions:

Waste Level

Waste / Month

Minimal

30 kg

Average

60 kg

High

100 kg

The project also contains recycling-related waste factors:

Recycling Level

kg CO₂/kg waste

High Recycling

0.42

Medium Recycling

0.89

Low Recycling

1.54

🏷️ Footprint Classification

Each emission category has its own thresholds.

Category

Low

Medium

High

Electricity

< 150

150–<300

≥ 300

Transport

< 80

80–<150

≥ 150

Industries

< 150

150–<300

≥ 300

Waste

< 40

40–<70

≥ 70

The overall footprint uses the worst individual category:

HIGH > MEDIUM > LOW

For example:

Electricity → Low
Transport   → Medium
Industries  → Low
Waste       → High

Overall → HIGH

🌳 Eco Twin Gamification System

Points

Saving a calculation → +10 points

Eco-actions award the number of points associated with the selected action.

Current action examples include:

Action

Points

Reduce Power Plants

+15

Improve Transport

+20

Happiness

Completing an eco-action increases Eco Twin happiness:

Happiness increase = +5
Maximum happiness = 100

Tree Growth

The tree contains five stages:

Stage 1 → Tiny seedling
Stage 2 → Small sprout
Stage 3 → Young sapling
Stage 4 → Growing tree
Stage 5 → Full-grown tree

The backend applies:

LOW footprint
    ↓
Advance one stage

MEDIUM footprint
    ↓
No stage change

HIGH footprint
    ↓
Move back one stage

When Stage 5 is completed through another low-footprint result:

Tree Level + 1
Stage → 1

🏗️ System Architecture

                         ┌──────────────────────┐
                         │        USER          │
                         └──────────┬───────────┘
                                    │
                                    ▼
                    ┌─────────────────────────────┐
                    │       WEB FRONTEND          │
                    │                             │
                    │ HTML + CSS + JavaScript    │
                    │ Jinja2 + Leaflet + Chart.js│
                    └─────────────┬───────────────┘
                                  │
                           HTTP / JSON
                                  │
                                  ▼
                    ┌─────────────────────────────┐
                    │        FLASK BACKEND        │
                    │            app.py            │
                    │                             │
                    │ • Page Routes               │
                    │ • API Endpoints             │
                    │ • Carbon Calculations       │
                    │ • Location Processing       │
                    │ • Weather / AQI             │
                    │ • Gamification              │
                    │ • Database Operations       │
                    └────────────┬────────────────┘
                                 │
                  ┌──────────────┴───────────────┐
                  │                              │
                  ▼                              ▼
        ┌──────────────────┐           ┌─────────────────────┐
        │    SQLite DB     │           │  External Services  │
        │   eco_twin.db    │           │                     │
        │                  │           │ • Nominatim         │
        │ • users          │           │ • OpenWeather       │
        │ • calculations   │           │ • OpenStreetMap     │
        │ • user_stats     │           │                     │
        └──────────────────┘           └─────────────────────┘

🛠️ Technology Stack

Technology

Role

Python

Backend programming language

Flask

Web framework

SQLite

Persistent database

HTML5

Page structure

CSS3

UI styling

JavaScript

Client-side functionality

Jinja2

Server-side templating

Requests

External HTTP/API requests

python-dotenv

Environment configuration

Leaflet.js

Interactive maps

OpenStreetMap

Map tiles

Chart.js

Carbon history visualization

Browser Geolocation API

User location

Nominatim

Reverse geocoding

OpenWeather

Weather and AQI data

Replit

Development/deployment configuration

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
│       ├── eco-twin-low.jpg
│       └── eco-twin-medium.jpg
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

Main Files

File

Description

app.py

Main Flask application, calculations, database logic, APIs, location services and gamification

eco_twin.db

Main SQLite database

templates/home.html

Landing/home page

templates/calculator.html

Carbon footprint calculator

templates/profile.html

Eco Twin profile and analytics

templates/suggestions.html

Sustainability suggestions, actions, events and nearby locations

static/css/style.css

Main stylesheet

static/images/

Eco Twin state images

.gitignore

Git ignore configuration

.replit

Replit configuration

replit.md

Replit/project development notes

The attached_assets/ directory contains development/source copies and project assets retained from the original project environment.

🌐 Web Pages

🏠 Home

Route:

/

The home page contains:

Eco Twin branding

Carbon-footprint introduction

Calculator navigation

Suggestions navigation

GPS/location feature information

Environmental API information

Dual calculation modes

Smart suggestions

Gamification information

Progress tracking

Daily eco-fact

🧮 Calculator

Route:

/calculator

The calculator contains:

Question Mode

Number Mode

Individual section selection

GPS location

Weather information

Carbon intensity

AQI

Interactive map

Carbon calculation

Emission breakdown chart

Result classification

New calculation functionality

👤 Profile

Route:

/profile

The profile contains:

Eco Twin visualization

Eco Tree

Tree level

Tree stage

Happiness

Points

Total calculations

Monthly emissions

Historical progress chart

Calculation history

💡 Suggestions

Route:

/suggestions

The Suggestions page contains tabs for:

All Suggestions

Power Plants

Transport

Industries

Waste

Events

It also includes:

Category-specific suggestions

Eco-actions

Point rewards

Map-based location cards

Sustainability events/workshops

🔌 API Reference

POST /api/calculate

Calculates emissions and saves the result to SQLite.

The endpoint:

Receives calculator data.

Determines the electricity factor.

Calculates category emissions.

Determines the overall category.

Saves the calculation.

Awards 10 points.

Updates the Eco Tree.

Returns the calculated result as JSON.

GET /api/weather

Returns weather information for supplied coordinates.

Parameters:

lat
lon

GET /api/geocode

Reverse-geocodes supplied coordinates.

Parameters:

lat
lon

GET /api/eco-events

Returns sustainability events based on footprint category.

Parameter:

category=low
category=medium
category=high

GET /api/profile-history-detailed

Returns the user's complete calculation history with category-wise emissions.

POST /api/delete-history

Deletes the user's stored calculation history and resets:

Total calculations

Tree level

GET /api/daily-fact

Returns a randomly selected:

Eco fact

Action tip

Analogy

POST /api/complete-action

Completes an eco-action and updates:

Points

Eco Twin happiness

GET /api/emission-intensity

Returns:

Regional electricity carbon intensity

AQI

AQI source

User coordinates

GET /api/profile/stats

Returns:

Total points

Happiness

Tree level

Total calculations

Current tree stage

GET /api/profile/latest

Returns the latest footprint:

Total CO₂

Category

GET /api/profile/history

Returns the latest ten calculations.

GET /api/profile/monthly-stats

Returns current-month aggregated:

Electricity

Transport

Industries

Waste

Total CO₂

🗄️ Database Schema

EcoSessionTree uses SQLite.

users

Column

Type

Description

id

INTEGER

Primary key

username

TEXT

Unique username

email

TEXT

User email

created_at

TIMESTAMP

Account creation time

The current application automatically creates a default user:

username: default_user
email: user@ecotwin.com

calculations

Column

Type

Description

id

INTEGER

Primary key

user_id

INTEGER

Associated user

electricity

REAL

Electricity CO₂

transport

REAL

Transport CO₂

diet

REAL

Industries / consumption CO₂

waste

REAL

Waste CO₂

total_co2

REAL

Total emissions

category

TEXT

Low / Medium / High

region

TEXT

State/region

input_mode

TEXT

Question / Number

calculated_at

TIMESTAMP

Calculation time

latitude

REAL

GPS latitude

longitude

REAL

GPS longitude

city_name

TEXT

City

state_name

TEXT

State

user_stats

Column

Type

Description

user_id

INTEGER

Primary key / user reference

total_points

INTEGER

Total points

eco_twin_happiness

INTEGER

Happiness score

tree_level

INTEGER

Tree level

current_tree_stage

INTEGER

Tree stage 1–5

total_calculations

INTEGER

Number of calculations

🌐 External Services

OpenStreetMap

Used as the map tile provider.

Leaflet

Used to display interactive maps in the browser.

Nominatim

Used for reverse geocoding.

Latitude + Longitude
        ↓
Nominatim
        ↓
City / State / Country

OpenWeather

Used for weather and air-quality information when an API key is available.

API Caching

The backend maintains an in-memory cache.

Cache duration = 300 seconds
               = 5 minutes

This reduces repeated requests to external services.

🔐 Environment Variables

The application reads configuration from environment variables using python-dotenv.

Required

SESSION_SECRET

The application exits during startup if SESSION_SECRET is not configured.

Generate a secure secret with:

python -c "import secrets; print(secrets.token_hex(32))"

Then configure the generated value in your local environment.

Optional

OPENWEATHER_API_KEY

This enables live weather and AQI information.

.gitignore

Environment files should remain outside Git:

.env
*.env

Never commit API keys, session secrets, passwords or other credentials.

If a secret has already been committed, deleting the file from the working directory does not remove it from Git history. The credential should be rotated/revoked and the history cleaned before publishing.

🚀 Installation

1. Clone the Repository

git clone https://github.com/priyanshushe/EcoSessionTree.git
cd EcoSessionTree

2. Create a Virtual Environment

Windows PowerShell

python -m venv .venv
.\.venv\Scripts\Activate.ps1

macOS / Linux

python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies

The current repository does not contain a requirements.txt, so install the Python packages used by app.py:

pip install Flask requests python-dotenv

4. Configure the Environment

Set the required SESSION_SECRET environment variable.

For live weather/AQI data, also configure:

OPENWEATHER_API_KEY

Keep these values outside Git.

5. Run the Application

python app.py

The application listens on:

http://127.0.0.1:5000

The Flask server binds to:

0.0.0.0:5000

which also supports hosted environments.

▶️ Replit Setup

The repository contains a .replit configuration.

The application is started using:

python app.py

and uses port:

5000

Configure these through Replit Secrets/environment variables:

SESSION_SECRET

Optional:

OPENWEATHER_API_KEY

🔒 Security & Privacy

Secrets

Do not commit .env files.

Do not commit API keys.

Do not expose SESSION_SECRET.

Rotate credentials if they have been exposed.

Location

The browser asks the user for permission before providing geolocation data.

The application uses latitude and longitude for:

Reverse geocoding

Regional electricity factors

Weather/AQI

Map display

Database

The current application uses a local SQLite database and a default user rather than a complete production authentication system.

Production Security

Before production deployment, the application should additionally consider:

Secure authentication

Authorization

CSRF protection

Input validation

Rate limiting

Secure cookie configuration

HTTPS

Production database

Production WSGI server

Proper secret management

Improved API error handling

⚠️ Important Implementation Notes

Carbon Estimates

EcoSessionTree provides estimates, not direct measurements of an individual's actual emissions.

Results depend on:

User inputs

Predefined assumptions

Emission factors

Regional electricity data

Selected transport type

Industries Database Field

The SQLite column:

diet

is retained from the original schema, but it represents:

Industries / Consumption CO₂

It is not currently used as a dietary-emissions field.

Number Mode Transport

Number Mode accepts monthly distance but currently applies the configured car emission factor:

0.192 kg CO₂/km

Eco Events

The events are generated from application-defined event lists.

They are not live event listings.

Nearby Locations

The Suggestions page contains application-defined nearby eco-friendly location cards and map directions rather than a live places-search API.

Weather & AQI

Live environmental information depends on the availability of the OpenWeather API configuration and external service response.

Database

SQLite is appropriate for a lightweight academic/project application. A production deployment with many concurrent users would benefit from a server-grade database.

🧪 Application Flow

A typical user journey is:

1. Open EcoSessionTree
        ↓
2. Read daily eco-fact
        ↓
3. Open Carbon Calculator
        ↓
4. Allow location access
        ↓
5. View location / weather / AQI
        ↓
6. Choose Question Mode or Number Mode
        ↓
7. Enter activity information
        ↓
8. Calculate footprint
        ↓
9. View CO₂ result and breakdown
        ↓
10. Receive Low / Medium / High classification
        ↓
11. Save calculation
        ↓
12. Earn points
        ↓
13. Eco Tree changes based on footprint
        ↓
14. Open Suggestions
        ↓
15. Complete eco-actions
        ↓
16. Earn additional points
        ↓
17. Track progress from Profile

📊 Example Calculation

Suppose a user enters:

Electricity = 300 kWh/month
Transport   = 600 km/month
Industries  = 280 kg CO₂/month
Waste       = 60 kg/month

Using Karnataka's configured electricity factor:

Electricity
= 300 × 0.690
= 207.00 kg CO₂

Transport in Number Mode:

Transport
= 600 × 0.192
= 115.20 kg CO₂

Industries:

Industries
= 280 kg CO₂

Waste:

Waste
= 60 × 0.89
= 53.40 kg CO₂

Total:

207.00
+ 115.20
+ 280.00
+ 53.40
----------------
655.60 kg CO₂/month

The category thresholds are then applied to each individual component to determine the overall footprint classification.

📈 Data Visualization

The Profile page uses Chart.js to visualize footprint history.

The dashboard can display:

Historical total CO₂

Calculation dates

Monthly category totals

Electricity contribution

Transport contribution

Industries contribution

Waste contribution

This allows users to observe changes in their footprint over repeated calculations.

🧠 Key Backend Components

The main Flask application contains the following functional components:

Database

init_db()
get_default_user()

Caching

get_cache_key()
get_from_cache()
set_to_cache()

Location

reverse_geocode()
get_electricity_factor()

Environmental APIs

fetch_weather()
fetch_air_quality()

Carbon Calculation

calculate_emissions()

Gamification / Events

generate_eco_events()

Web Pages

home()
calculator()
profile()
suggestions()

APIs

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

🚀 Future Enhancements

Full user registration and authentication

Secure password-based authentication

PostgreSQL/MySQL production database

Live nearby eco-friendly place discovery

Live sustainability event discovery

Vehicle-specific carbon calculations

More detailed food/dietary footprint calculations

Renewable-energy recommendations

Carbon-offset recommendations

PDF carbon reports

CSV export

Monthly sustainability reports

Advanced analytics

Personal carbon-reduction goals

Community challenges

Leaderboards

Achievement badges

Progressive Web App support

Cloud deployment

Automated testing and CI/CD

Production logging and monitoring

🎓 Academic / Technical Learning Outcomes

This project demonstrates practical implementation of:

Python programming

Flask web development

REST-style API development

HTML5

CSS3

Vanilla JavaScript

Jinja2 templating

SQLite database design

CRUD-style database operations

External API integration

Browser Geolocation API

Reverse geocoding

Interactive maps

Data visualization

Session storage

Environment-variable configuration

Caching

Gamification

Environmental data processing

Full-stack application development

📦 Dependencies

The backend uses:

Flask
requests
python-dotenv

Frontend libraries/services include:

Leaflet.js
OpenStreetMap
Chart.js
Browser Geolocation API

🧰 Development

Start the application with:

python app.py

The current Flask configuration runs with:

Host: 0.0.0.0
Port: 5000
Debug: enabled in the current source configuration

For production deployment, debug mode should be disabled and a production WSGI server should be used.

🌐 Repository

GitHub Repository:

https://github.com/priyanshushe/EcoSessionTree

📄 License

No explicit open-source license is currently included in this repository.

Without a license, the project should be treated as all rights reserved. Add an appropriate LICENSE file if you want to formally permit reuse, modification or redistribution.

<div align="center">

🌱 Measure your impact. Make better choices. Grow your Eco Twin.

EcoSessionTree • Eco Twin

</div>
