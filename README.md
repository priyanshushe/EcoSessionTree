::: {align="center"}

🌱 EcoSessionTree

Turn everyday activities into a measurable carbon footprint --- and grow your Eco Twin.

A location-aware Flask web application that estimates monthly CO₂
emissions, visualizes environmental impact, and uses gamification
to encourage more sustainable choices.

<br>{=html}






:::

📌 Table of Contents

Overview

Key Features

How It Works

Carbon Calculation

Gamification

Technology Stack

Application Architecture

Project Structure

Application Routes

API Reference

Database Design

External Services

Environment Variables

Local Installation

Running on Replit

Security Notes

Current Scope & Limitations

Future Enhancements

License

🌍 Overview

EcoSessionTree is a sustainability-focused web application designed
to help users understand the environmental impact of everyday
activities.

The application estimates a user's monthly carbon footprint across four
areas:

⚡ Electricity

🚗 Transport

🏭 Industries / Consumption

🗑️ Waste

Users can either answer simple lifestyle questions or enter numerical
values directly. The application then calculates the estimated
footprint, classifies the result as Low, Medium, or High,
stores the calculation in SQLite, and updates an interactive Eco
Twin progression system.

The project combines:

Carbon tracking + location awareness + environmental information +
analytics + gamification

✨ Key Features

🌱 Carbon Footprint Calculator

Estimates monthly CO₂ emissions in kg CO₂/month.

Displays the annual equivalent in tonnes CO₂/year.

Provides a category-wise emission breakdown.

Classifies the footprint as Low, Medium, or High.

Uses the highest-severity category as the overall footprint
classification.

❓ Question Mode

Designed for users who do not know their exact monthly consumption.

Users answer qualitative questions such as:

Electricity usage level

Primary transport type

Industrial/consumption impact

Waste generation level

The application converts these selections into predefined monthly
activity estimates.

🔢 Number Mode

For users who know their approximate consumption, the application
accepts numerical monthly values for:

Electricity --- kWh/month

Transport --- km/month

Industries / consumption --- kg CO₂/month

Waste --- kg/month

📍 Location Awareness

The browser's Geolocation API is used to obtain latitude and
longitude.

The coordinates can then be used for:

Reverse geocoding

Regional electricity emission factors

Map visualization

Weather information

Air-quality information

🗺️ Interactive Map

The calculator uses Leaflet.js with OpenStreetMap tiles to
display the detected location.

🌤️ Weather & AQI

When an OpenWeather API key is configured, the application can retrieve:

Temperature

Weather description

Humidity

Wind speed

Air Quality Index

Fallback values are used when the API key is unavailable, so the core
calculator can still operate.

📊 Profile Dashboard

The profile dashboard presents:

Total points

Eco Twin happiness

Total calculations

Tree level and stage

Latest footprint category

Monthly emissions

Category-wise emissions

Historical footprint chart

Recent calculation history

🌳 Gamification

The application turns sustainability tracking into a progression system:

Saved calculations award points.

Completed eco-actions award additional points.

Eco Twin happiness increases after completed actions.

Low-emission results can advance the tree.

High-emission results can reduce the tree stage.

Completing all five stages advances the tree level.

💡 Eco Suggestions

Users can browse recommendations related to:

Electricity

Transportation

Industries / consumption

Waste

Actions can be marked as completed to earn points.

🌿 Eco Events & Workshops

The application includes sustainability-focused event/workshop content
and an API that generates category-specific event suggestions.

📈 Calculation History

Each saved calculation records information such as:

Total CO₂

Category

Calculation time

Location

Coordinates

Category-wise emissions

Input mode

💾 Session Persistence

The calculator stores its current state in browser sessionStorage,
allowing the latest calculator state to be restored during the same
browser session.

🔄 How It Works

┌───────────────────────┐
│       User opens      │
│      EcoSessionTree   │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│      Open Calculator   │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────────────┐
│ Browser Geolocation API        │
│ Latitude + Longitude           │
└───────────┬───────────────────┘
            │
            ├──────────────► Reverse Geocoding
            ├──────────────► Regional Carbon Factor
            ├──────────────► Weather / AQI
            └──────────────► Interactive Map
            │
            ▼
┌───────────────────────────────┐
│ Choose calculation mode       │
│                               │
│ Question Mode  /  Number Mode │
└───────────┬───────────────────┘
            │
            ▼
┌───────────────────────────────┐
│ Emission Calculation Engine   │
│ Electricity + Transport +     │
│ Industries + Waste            │
└───────────┬───────────────────┘
            │
            ▼
┌───────────────────────────────┐
│ Footprint Result               │
│ kg CO₂/month + category        │
└───────────┬───────────────────┘
            │
            ▼
┌───────────────────────────────┐
│ SQLite                         │
│ Save calculation + update      │
│ points / tree / happiness      │
└───────────┬───────────────────┘
            │
            ▼
┌───────────────────────────────┐
│ Profile Dashboard              │
│ History + charts + Eco Twin    │
└───────────────────────────────┘

🧮 Carbon Calculation

The core calculation follows:

Total CO₂ = Electricity + Transport + Industries + Waste

⚡ Electricity

Electricity CO₂ = Monthly Electricity × Regional Emission Factor

The application contains regional electricity factors and a global
fallback.

Fallback:

0.475 kg CO₂/kWh

🚗 Transport

Transport CO₂ = Monthly Distance × Transport Emission Factor

The application contains predefined factors for several transport types,
including:

Walking

Bicycle

Public transport

Car

SUV

Motorcycle

Electric car

Hybrid

Train

Metro

Bus

Short-haul flight

Long-haul flight

Question Mode uses predefined assumptions for supported transport
choices.

🏭 Industries / Consumption

Question Mode uses predefined monthly estimates:

Level      Estimated CO₂

Low         120 kg/month
Medium      280 kg/month
High        580 kg/month

Number Mode accepts the user's industrial/consumption CO₂ value
directly.

🗑️ Waste

Waste CO₂ = Monthly Waste × Waste Emission Factor

The current average waste factor is:

0.89 kg CO₂/kg waste

🏷️ Footprint Classification

Each category uses its own thresholds.

Category                    Low                Medium             High

Electricity     < 150 kg/month   150--<300 kg/month   ≥ 300 kg/month
Transport        < 80 kg/month    80--<150 kg/month   ≥ 150 kg/month
Industries      < 150 kg/month   150--<300 kg/month   ≥ 300 kg/month
Waste            < 40 kg/month     40--<70 kg/month    ≥ 70 kg/month

The overall footprint is determined by the most severe category:

High > Medium > Low

🌳 Gamification

EcoSessionTree uses an Eco Twin system to make environmental tracking
more engaging.

Points

Each saved calculation → +10 points

Completing an eco-action → additional points

Happiness

Eco Twin happiness increases when actions are completed and is capped
at:

100

Tree Progression

The tree has 5 stages.

Low footprint → tree can advance

Medium footprint → tree stage remains unchanged

High footprint → tree can regress

After completing all five stages, the tree level advances and the stage
resets.

🛠️ Technology Stack

Layer                    Technology

Backend                  Python 3.11
Web Framework            Flask
Frontend                 HTML5, CSS3, JavaScript
Templating               Jinja2
Database                 SQLite
HTTP/API Client          Requests
Environment Management   python-dotenv
Maps                     Leaflet.js
Map Data                 OpenStreetMap
Charts                   Chart.js
Location                 Browser Geolocation API
Deployment Environment   Replit

🏗️ Application Architecture

EcoSessionTree follows a lightweight monolithic Flask architecture.

                    ┌─────────────────────┐
                    │     Web Browser     │
                    │                     │
                    │ HTML + CSS + JS     │
                    │ Jinja2              │
                    │ Leaflet + Chart.js  │
                    │ Geolocation API     │
                    └──────────┬──────────┘
                               │
                         HTTP / JSON
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Flask App      │
                    │       app.py        │
                    │                     │
                    │ • Page Routes       │
                    │ • API Routes        │
                    │ • CO₂ Calculations  │
                    │ • Location Services │
                    │ • Weather / AQI     │
                    │ • Gamification      │
                    │ • Caching           │
                    └───────┬───────┬─────┘
                            │       │
                 ┌──────────┘       └───────────┐
                 ▼                              ▼
        ┌─────────────────┐            ┌──────────────────┐
        │   SQLite DB     │            │ External Services│
        │  eco_twin.db    │            │                  │
        │                 │            │ • Nominatim      │
        │ • users         │            │ • OpenWeather    │
        │ • calculations  │            │ • OSM Tiles      │
        │ • user_stats    │            │                  │
        └─────────────────┘            └──────────────────┘

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
    └── Development/source assets retained from the project environment

Core Files

File                                Responsibility

app.py                            Flask server, routes, APIs,
database logic, calculations,
location services and gamification

eco_twin.db                       SQLite database

templates/home.html               Landing page and eco-fact

templates/calculator.html         Carbon calculator

templates/profile.html            Profile, statistics, charts and
history

templates/suggestions.html        Suggestions, actions, events and
location cards

static/css/style.css              Application styling

static/images/                    Eco Twin state images

.gitignore                        Prevents environment files from
being committed

.replit                           Replit configuration

replit.md                         Project/development notes

🌐 Application Routes

Route                   Method                  Description

/                     GET                     Landing page with daily
eco-fact

/calculator           GET                     Carbon footprint
calculator

/profile              GET                     Profile, statistics and
calculation history

🔌 API Reference

Endpoint                          Method                  Purpose

/api/calculate                  POST                    Calculates and stores a
carbon footprint

/api/weather                    GET                     Retrieves weather
information

/api/geocode                    GET                     Reverse-geocodes
coordinates

/api/eco-events                 GET                     Returns category-based
eco events

/api/profile-history-detailed   GET                     Returns detailed
calculation history

/api/delete-history             POST                    Deletes calculation
history and resets core
progress

/api/daily-fact                 GET                     Returns an eco fact,
action tip and analogy

/api/complete-action            POST                    Completes an eco-action
and awards points

/api/emission-intensity         GET                     Returns regional carbon
intensity and AQI
information

/api/profile/stats              GET                     Returns profile
statistics

/api/profile/latest             GET                     Returns the latest
footprint

/api/profile/history            GET                     Returns the latest 10
calculations

📦 Calculation API Examples

Question Mode

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

Number Mode

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

🗄️ Database Design

The project uses SQLite for simple, zero-configuration local
persistence.

users

Column         Purpose

id           Primary key
username     Unique username
email        User email
created_at   Account creation timestamp

calculations

Column            Purpose

id              Primary key
user_id         Associated user
electricity     Electricity CO₂
transport       Transport CO₂
diet            Stores the industries/consumption emission value
waste           Waste CO₂
total_co2       Total CO₂
category        Low, Medium or High
region          Region/state
input_mode      Question or Number
calculated_at   Calculation timestamp
latitude        GPS latitude
longitude       GPS longitude
city_name       City/locality
state_name      State

user_stats

Column                 Purpose

user_id              User identifier
total_points         Accumulated points
eco_twin_happiness   Happiness score
tree_level           Tree level
current_tree_stage   Current stage from 1--5
total_calculations   Number of calculations

🌐 External Services

OpenStreetMap + Leaflet

Used for map rendering and map tiles.

The application uses Leaflet.js on the frontend and OpenStreetMap-based
services for location visualization.

Nominatim

Used for reverse geocoding:

Latitude + Longitude
        ↓
Nominatim
        ↓
City / State / Country

OpenWeather

Used for current weather and air-quality data when:

OPENWEATHER_API_KEY

is configured.

Response Caching

External location/weather/AQI responses are cached in memory for
approximately 5 minutes to reduce repeated requests.

🔐 Environment Variables

The application uses python-dotenv and environment variables for
configuration.

Required

SESSION_SECRET=your-generated-secret

SESSION_SECRET is required because Flask uses it to sign session data.

Generate a secure value with:

python -c "import secrets; print(secrets.token_hex(32))"

Optional

OPENWEATHER_API_KEY=your-openweather-api-key

This enables live OpenWeather weather/AQI information.

Never Commit Secrets

The project ignores environment files:

.env
*.env

Do not commit API keys, session secrets, passwords, or other
credentials to GitHub.

If a real credential has already been committed, simply deleting .env
is not enough. The exposed credential should be revoked/rotated, and
the Git history should be cleaned before publishing.

🚀 Local Installation

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

The current project does not include a requirements.txt, so install
the packages used by app.py:

pip install Flask requests python-dotenv

4. Configure Environment Variables

Create a local .env file:

SESSION_SECRET=<generated-secret>
OPENWEATHER_API_KEY=<optional-openweather-key>

Keep .env local and never commit it.

5. Start the Application

python app.py

The application runs on:

http://127.0.0.1:5000

The Flask server is configured to bind to:

0.0.0.0:5000

which is also suitable for hosted environments such as Replit.

▶️ Running on Replit

The repository contains a .replit configuration for the project.

The configured workflow starts the Flask application with:

python app.py

and uses port:

5000

Before running on Replit, add the following through the Replit
Secrets/environment configuration:

SESSION_SECRET

Optionally add:

OPENWEATHER_API_KEY

🔒 Security Notes

Keep .env outside Git history.

Never expose SESSION_SECRET.

Never commit API keys.

Rotate credentials if they were previously exposed.

Browser geolocation requires user permission.

External API availability can affect weather/AQI and
reverse-geocoding features.

The project uses SQLite and is primarily designed as a lightweight
application/demo rather than a production multi-user deployment.

⚠️ Current Scope & Limitations

A few implementation details are worth knowing before deploying the
project publicly:

The application is a carbon-footprint estimator. Its output
depends on predefined emission factors and user-provided/assumed
activity values.

Number Mode transport currently applies the application's car
factor to the supplied monthly distance.

Nearby eco-friendly locations are application-defined cards, not
results from a live places database.

Eco events/workshops are curated/generated application content,
not a live event-search feed.

Weather/AQI requires OpenWeather configuration for live data.

The application uses a lightweight local SQLite database, which
is suitable for development and demonstration but would need a more
robust database/deployment architecture for larger production
workloads.

Authentication is lightweight in the current implementation
rather than a full production authentication system.

🚀 Future Enhancements

Potential extensions for EcoSessionTree include:

User authentication and secure account management

PostgreSQL or another production-grade database

Live eco-friendly place discovery

Live sustainability event discovery

More detailed dietary carbon calculations

Vehicle-specific transport calculations

Carbon-offset recommendations

Monthly and yearly sustainability reports

Export footprint history as PDF/CSV

More advanced analytics and dashboards

Mobile-responsive progressive web app

Personalized sustainability goals

Leaderboards and community challenges

Cloud deployment with production monitoring

📚 Learning & Project Context

EcoSessionTree demonstrates the integration of several practical
software-development concepts in one application:

Flask web development

REST-style APIs

Jinja2 templating

Client-side JavaScript

Browser geolocation

Reverse geocoding

External API integration

SQLite database design

Data visualization

Environmental data processing

Gamification

Session/state management

Environment-based configuration

It can therefore serve as a practical project for demonstrating
full-stack web development, API integration, database management, and
sustainability-focused software design.

📄 License

No explicit open-source license is currently included in the repository.

Unless a license is added, the project should be treated as all rights
reserved by the copyright holder. Add an appropriate LICENSE file
before granting others permission to reuse, modify, or redistribute the
code.

👨‍💻 Project Repository

EcoSessionTree

GitHub: https://github.com/priyanshushe/EcoSessionTree

::: {align="center"}

🌱 Measure your impact. Make better choices. Grow your Eco Twin.

EcoSessionTree
:::
