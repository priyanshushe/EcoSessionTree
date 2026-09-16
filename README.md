<div align="center">

# 🌱 EcoSessionTree

## Track Your Carbon. Grow Your Eco Twin. Build a Greener Future.

**A sustainability-focused Flask web application for carbon-footprint tracking, environmental analytics, eco-friendly actions, and gamified Eco Twin growth.**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web_Framework-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)

**🌍 Carbon Tracking · 📊 Analytics · 🌳 Gamification · 📍 Location · 🌤️ Weather · ♻️ Sustainability**

</div>

---

## 📌 Table of Contents

- [🌍 About the Project](#-about-the-project)
- [🎯 Why EcoSessionTree](#-why-ecsessiontree)
- [✨ Core Features](#-core-features)
- [🧮 Carbon Footprint Calculation](#-carbon-footprint-calculation)
- [🌳 Eco Twin & Gamification](#-eco-twin--gamification)
- [🧩 Application Modules](#-application-modules)
- [🛠️ Technology Stack](#-technology-stack)
- [🏗️ System Architecture](#-system-architecture)
- [📁 Project Structure](#-project-structure)
- [🗄️ Database Design](#-database-design)
- [🔌 API Documentation](#-api-documentation)
- [🚀 Installation](#-installation)
- [🔐 Configuration](#-configuration)
- [▶️ Running the Application](#-running-the-application)
- [🧭 How to Use](#-how-to-use)
- [📊 Environmental Classification](#-environmental-classification)
- [⚡ Caching](#-caching)
- [📍 Location & Weather](#-location--weather)
- [🛡️ Security](#-security)
- [⚠️ Current Limitations](#-current-limitations)
- [🔮 Future Improvements](#-future-improvements)
- [📚 Learning Outcomes](#-learning-outcomes)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [👨‍💻 Author](#-author)

---

## 🌍 About the Project

**EcoSessionTree** is a sustainability-focused web application designed to make carbon-footprint tracking **simple, interactive, and engaging**.

Instead of presenting environmental impact as only a number, EcoSessionTree turns everyday lifestyle information into an interactive sustainability experience.

The application allows users to:

- ⚡ Calculate estimated **electricity emissions**
- 🚗 Estimate **transportation emissions**
- 🛍️ Estimate **industries / consumption emissions**
- ♻️ Estimate **waste emissions**
- 📊 View their **overall carbon footprint**
- 🌳 Grow a virtual **Eco Twin tree**
- ⭐ Earn **eco points**
- 😊 Increase Eco Twin **happiness**
- 📈 Review **calculation history**
- 📅 View **monthly statistics**
- 📍 Use location information for regional calculations
- 🌤️ Retrieve weather and air-quality information
- 💡 Discover sustainability tips and facts
- 🌱 Complete eco-friendly actions
- 📍 Explore application-provided eco events and locations

> **💡 Core idea:** The more sustainable your lifestyle becomes, the healthier your Eco Twin becomes.

---

## 🎯 Why EcoSessionTree?

Traditional carbon calculators often stop after displaying a result. EcoSessionTree adds an interactive feedback loop that connects **measurement → feedback → action → progress**.

```text
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
Improved Habits
      ↓
Lower Estimated Footprint
```

This approach makes sustainability **visual, measurable, and engaging**.

---

## ✨ Core Features

### ⚡ 1. Carbon Footprint Calculator

Users can calculate estimated monthly CO₂ emissions across four major categories:

| Category | Represents |
|---|---|
| ⚡ **Electricity** | Household electricity consumption |
| 🚗 **Transport** | Monthly transportation activity |
| 🛍️ **Industries / Consumption** | Lifestyle and consumption impact |
| ♻️ **Waste** | Monthly waste generation |

The final footprint is calculated as:

```text
Total CO₂ = Electricity CO₂ + Transport CO₂ + Industries CO₂ + Waste CO₂
```

### 📊 2. Environmental Impact Classification

Each category is classified as:

- 🟢 **LOW**
- 🟡 **MEDIUM**
- 🔴 **HIGH**

The overall classification follows the highest-impact category.

```text
HIGH > MEDIUM > LOW
```

### 🌳 3. Eco Twin

The **Eco Twin** is the central gamification element of the application.

It represents the user's sustainability journey through:

- ❤️ Happiness
- ⭐ Eco points
- 🌱 Tree stage
- 🌲 Tree level
- 📊 Sustainability history

### ⭐ 4. Eco Points

Users earn points for sustainable actions.

Examples include:

| Action | Points |
|---|---:|
| **Saving calculation** | +10 |
| **Reduce Power Plants** | +15 |
| **Improve Transport** | +20 |

### 😊 5. Eco Twin Happiness

Completing an eco-friendly action increases happiness by **5 points**, with a maximum happiness value of **100**.

```text
Eco Action Completed
        ↓
     +5 Happiness
        ↓
Maximum = 100
```

### 📈 6. Historical Tracking

Carbon calculations can be stored and reviewed later, including:

- Previous calculations
- Total CO₂
- Category
- Region
- Input mode
- Date and time
- Location information

### 📅 7. Monthly Statistics

The profile dashboard provides monthly statistics for understanding changes in estimated carbon footprint over time.

### 💡 8. Sustainability Suggestions

The suggestions module provides actions and recommendations around:

- Energy conservation
- Sustainable transportation
- Waste reduction
- Lifestyle choices

### 🌤️ 9. Weather & Air Quality

When an OpenWeather API key is configured, the application can retrieve weather and air-quality information.

### 📍 10. Location Awareness

Browser geolocation can provide coordinates used for:

- Regional electricity emission factors
- Reverse geocoding
- City and state information
- Weather information

### 📚 11. Daily Eco Facts

The application can display sustainability-related facts, tips, and environmental analogies on the home page.

---

## 🧮 Carbon Footprint Calculation

EcoSessionTree divides estimated emissions into four major categories.

### ⚡ Electricity Emissions

```text
Electricity CO₂
=
Monthly Electricity Consumption
×
Regional Emission Factor
```

Supported regional factors include:

| Region | Factor (kg CO₂/kWh) |
|---|---:|
| India | 0.708 |
| Karnataka | 0.690 |
| Maharashtra | 0.720 |
| Tamil Nadu | 0.650 |
| Kerala | 0.120 |
| Delhi | 0.730 |
| Gujarat | 0.680 |
| Uttar Pradesh | 0.760 |
| West Bengal | 0.680 |

A global fallback factor of **0.475 kg CO₂/kWh** is used when a more specific factor is unavailable.

### 🚗 Transportation Emissions

```text
Transport CO₂
=
Monthly Distance
×
Transport Emission Factor
```

| Transport Mode | kg CO₂/km |
|---|---:|
| Walking | 0.000 |
| Bicycle | 0.000 |
| Public Transport | 0.041 |
| Car | 0.192 |
| Small Car | 0.145 |
| Medium Car | 0.192 |
| Large Car / SUV | 0.245 |
| Motorcycle | 0.103 |
| Electric Car | 0.053 |
| Hybrid | 0.119 |
| Train | 0.041 |
| Metro | 0.031 |
| Bus | 0.089 |
| Short-haul Flight | 0.255 |
| Long-haul Flight | 0.195 |

### 🛍️ Industries / Consumption

The application supports two input modes.

#### Question Mode

| Level | Estimated CO₂ |
|---|---:|
| Low | 120 kg/month |
| Medium | 280 kg/month |
| High | 580 kg/month |

#### Number Mode

Users can directly enter an estimated value in **kg CO₂/month**.

### ♻️ Waste Emissions

```text
Waste CO₂
=
Monthly Waste
×
Waste Emission Factor
```

The average waste factor is **0.89 kg CO₂/kg waste**.

Question-mode assumptions:

| Waste Level | Waste / Month |
|---|---:|
| Minimal | 30 kg |
| Average | 60 kg |
| High | 100 kg |

Recycling-related factors:

| Recycling Level | Factor |
|---|---:|
| High Recycling | 0.42 |
| Medium Recycling | 0.89 |
| Low Recycling | 1.54 |

> **Note:** These values are application-configured estimation factors used by the project and should not be interpreted as universal scientific constants.

---

## 🌳 Eco Twin & Gamification

EcoSessionTree connects environmental performance with a virtual ecosystem.

### 🌱 Tree Growth Stages

| Stage | Tree Growth |
|---:|---|
| 1 | 🌱 Tiny Seedling |
| 2 | 🌿 Small Sprout |
| 3 | 🌳 Young Sapling |
| 4 | 🌲 Growing Tree |
| 5 | 🌲 Full-Grown Tree |

After completing all five stages, the **tree level increases** and the growth cycle resets to stage 1.

### 📉 Footprint → Tree Behavior

| Environmental Result | Tree Effect |
|---|---|
| 🟢 **LOW** | Tree progresses |
| 🟡 **MEDIUM** | Current stage remains unchanged |
| 🔴 **HIGH** | Tree regresses |

This gives users a visual representation of their sustainability progress.

---

## 🧩 Application Modules

### 🏠 Home

The landing page introduces the project and provides sustainability information, daily eco facts, and navigation to the main features.

### 🧮 Calculator

The calculator handles:

- Electricity input
- Transport input
- Consumption input
- Waste input
- Regional factors
- CO₂ calculation
- Environmental classification
- Result presentation
- Calculation persistence

### 👤 Profile

The profile/dashboard provides:

- Eco points
- Eco Twin happiness
- Tree level
- Tree stage
- Total calculations
- Latest footprint
- Calculation history
- Monthly statistics

### 💡 Suggestions

The suggestions section provides:

- Eco-friendly actions
- Sustainability recommendations
- Eco events
- Application-provided eco locations
- Action completion

---

## 🛠️ Technology Stack

### Backend

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Flask** | Web framework |
| **SQLite** | Persistent database |
| **Requests** | External API communication |
| **python-dotenv** | Environment variable management |

### Frontend

| Technology | Purpose |
|---|---|
| **HTML5** | Page structure |
| **CSS3** | User interface styling |
| **JavaScript** | Client-side logic |
| **Jinja2** | Server-side templating |
| **Chart.js** | Data visualization |
| **Leaflet.js** | Interactive maps |

### External Services

| Service | Usage |
|---|---|
| **OpenWeather** | Weather and air-quality information |
| **OpenStreetMap** | Map data |
| **Nominatim** | Geocoding / reverse geocoding |
| **Browser Geolocation API** | User location |

---

## 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │      Web Browser     │
                         │   HTML / CSS / JS    │
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
        │ Waste          │ │ Eco Actions    │ │                 │
        └───────┬────────┘ └───────┬────────┘ └─────────────────┘
                │                  │
                └─────────┬────────┘
                          ▼
                 ┌──────────────────┐
                 │      SQLite      │
                 │   eco_twin.db    │
                 └──────────────────┘
```

---

## 📁 Project Structure

```text
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
```

> **Note:** `attached_assets/` contains development/source copies and supporting assets. The main application uses the files under `templates/` and `static/`.

---

## 🗄️ Database Design

EcoSessionTree uses **SQLite** for persistent application data.

### 👤 `users`

Stores basic user information.

| Column | Type |
|---|---|
| `id` | INTEGER |
| `username` | TEXT |
| `email` | TEXT |
| `created_at` | TIMESTAMP |

### 📊 `calculations`

Stores carbon-footprint calculations.

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Calculation ID |
| `user_id` | INTEGER | Associated user |
| `electricity` | REAL | Electricity emissions |
| `transport` | REAL | Transport emissions |
| `diet` | REAL | Industries / consumption emissions |
| `waste` | REAL | Waste emissions |
| `total_co2` | REAL | Total estimated emissions |
| `category` | TEXT | LOW / MEDIUM / HIGH |
| `region` | TEXT | Calculation region |
| `input_mode` | TEXT | Input method |
| `calculated_at` | TIMESTAMP | Calculation timestamp |
| `latitude` | REAL | Latitude |
| `longitude` | REAL | Longitude |
| `city_name` | TEXT | City |
| `state_name` | TEXT | State |

### 📈 `user_stats`

Stores Eco Twin progress.

| Column | Type |
|---|---|
| `user_id` | INTEGER |
| `total_points` | INTEGER |
| `eco_twin_happiness` | INTEGER |
| `tree_level` | INTEGER |
| `current_tree_stage` | INTEGER |
| `total_calculations` | INTEGER |

---

## 🔌 API Documentation

| Endpoint | Method | Purpose |
|---|---|---|
| `/api/calculate` | `POST` | Calculate and store carbon footprint |
| `/api/weather` | `GET` | Retrieve weather information |
| `/api/geocode` | `GET` | Reverse geocode coordinates |
| `/api/eco-events` | `GET` | Retrieve eco events |
| `/api/profile-history-detailed` | `GET` | Retrieve detailed calculation history |
| `/api/delete-history` | `POST` | Delete calculation history |
| `/api/daily-fact` | `GET` | Retrieve daily sustainability fact |
| `/api/complete-action` | `POST` | Complete an eco action |
| `/api/emission-intensity` | `GET` | Retrieve emission-intensity information |
| `/api/profile/stats` | `GET` | Retrieve profile statistics |
| `/api/profile/latest` | `GET` | Retrieve latest calculation |
| `/api/profile/history` | `GET` | Retrieve profile history |
| `/api/profile/monthly-stats` | `GET` | Retrieve monthly statistics |

### Important Backend Functions

```text
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
```

### Main Flask Routes

```text
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
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/priyanshushe/EcoSessionTree.git
cd EcoSessionTree
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install Flask requests python-dotenv
```

---

## 🔐 Configuration

EcoSessionTree uses environment variables for sensitive configuration.

### Required Variable

```text
SESSION_SECRET
```

### Optional Variable

```text
OPENWEATHER_API_KEY
```

The OpenWeather key is required only for the weather and air-quality integration.

### Generate a Secure Session Secret

Run:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Use the generated value as `SESSION_SECRET`.

### Local `.env` Configuration

Create a local `.env` file containing your actual credentials:

```text
SESSION_SECRET=YOUR_GENERATED_SESSION_SECRET
OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY
```

> **🔒 Never commit `.env` files or real API keys to GitHub.**

Recommended `.gitignore` entries:

```gitignore
.env
*.env
.venv/
__pycache__/
*.pyc
```

---

## ▶️ Running the Application

Start the Flask application with:

```bash
python app.py
```

The application is available locally at:

```text
http://127.0.0.1:5000
```

The server is configured to bind to:

```text
0.0.0.0:5000
```

Open the local address in a browser to use EcoSessionTree.

---

## 🧭 How to Use

### 1. 🏠 Open the Home Page

Explore the project introduction, Eco Twin concept, and sustainability information.

### 2. 🧮 Open the Calculator

Navigate to:

```text
/calculator
```

### 3. 📝 Enter Lifestyle Information

Provide information about:

- Electricity consumption
- Transportation
- Consumption / lifestyle
- Waste

### 4. 📊 Calculate Your Footprint

The application calculates category-level emissions and produces an overall classification.

### 5. 🌳 Review Your Eco Twin

Your environmental result affects:

- **Tree stage**
- **Eco points**
- **Happiness**
- **Profile statistics**

### 6. 💡 Complete Eco Actions

Navigate to:

```text
/suggestions
```

Complete sustainable actions to earn points and improve your Eco Twin.

### 7. 👤 Track Your Progress

Navigate to:

```text
/profile
```

You can view your latest footprint, history, monthly statistics, points, happiness, and tree progress.

---

## 📊 Environmental Classification

Each category is classified independently.

| Category | 🟢 LOW | 🟡 MEDIUM | 🔴 HIGH |
|---|---:|---:|---:|
| Electricity | < 150 | 150 – < 300 | ≥ 300 |
| Transport | < 80 | 80 – < 150 | ≥ 150 |
| Industries | < 150 | 150 – < 300 | ≥ 300 |
| Waste | < 40 | 40 – < 70 | ≥ 70 |

The overall result follows the highest-impact category:

```text
LOW
 ↓
MEDIUM
 ↓
HIGH
```

---

## ⚡ Caching

External API requests can be repeated frequently, so EcoSessionTree includes an **in-memory caching mechanism**.

Cached API information can remain available for approximately **5 minutes**.

The backend includes:

```text
get_cache_key()
get_from_cache()
set_to_cache()
```

Caching helps reduce unnecessary external requests and improves responsiveness.

---

## 📍 Location & Weather

EcoSessionTree can use browser-based geolocation after the user grants location permission.

### Location Flow

```text
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
```

### Weather Flow

```text
User Location
      ↓
Coordinates
      ↓
OpenWeather API
      ↓
Weather / AQI Information
      ↓
Application UI
```

Location access depends on browser permission and availability of the relevant external services.

---

## 🛡️ Security

EcoSessionTree follows basic security practices for configuration and local development.

### 🔐 Environment Secrets

Sensitive values such as:

- `SESSION_SECRET`
- `OPENWEATHER_API_KEY`

should be kept outside the source code.

### 🚫 Git Ignore

Environment files should be excluded from Git:

```gitignore
.env
*.env
```

### 📍 Location Permission

The browser requests permission before providing location data.

### 🔒 Production Security Recommendations

Before public production deployment, consider implementing:

- **Production-grade authentication**
- **Authorization**
- **CSRF protection**
- **Input validation**
- **Rate limiting**
- **Secure cookies**
- **HTTPS**
- **Production WSGI server**
- **Centralized secret management**
- **Production database**
- **Stronger API error handling**

---

## ⚠️ Current Limitations

### Authentication

The current implementation uses a lightweight/default-user approach rather than a complete production authentication system.

### Eco Locations

Nearby eco-friendly locations are application-defined rather than being retrieved from a live places-discovery service.

### Eco Events

Eco events are application-defined rather than continuously synchronized with an external event database.

### Database

SQLite is appropriate for development and smaller deployments but may not be suitable for large production workloads.

### Flask Debug Mode

The current development configuration uses Flask debug mode. **Debug mode should be disabled for production.**

---

## 🔮 Future Improvements

### 🔐 User Authentication

- User registration
- Login/logout
- Password hashing
- Email verification
- OAuth authentication
- User-specific dashboards

### 📊 Advanced Analytics

- Weekly trends
- Yearly trends
- Category comparisons
- Carbon-reduction percentages
- Personal sustainability goals
- Interactive dashboards

### 🤖 AI-Based Recommendations

A recommendation engine could analyze a user's footprint and generate personalized sustainability suggestions.

```text
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
```

### 🌍 Real-Time Eco Locations

Live places APIs could provide information about:

- Recycling centers
- EV charging stations
- Public transport
- Organic stores
- Sustainable businesses
- Green spaces

### 🏆 Community Leaderboards

Possible leaderboard categories include:

- Individual progress
- College/community progress
- Monthly challenges
- Sustainability achievements

### 🎯 Sustainability Challenges

Examples:

- 🚲 **Car-Free Week**
- 💡 **Energy Saving Challenge**
- ♻️ **Zero-Waste Week**
- 🌳 **Tree Plantation Challenge**
- 🚆 **Public Transport Challenge**

### 📱 Mobile Application

The backend could be extended into an API-driven mobile application using technologies such as React Native or Flutter.

### ☁️ Production Deployment

A possible production architecture:

```text
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
```

---

## 🧪 Example User Journey

```text
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
```

---

## 💡 Design Philosophy

EcoSessionTree is built around three principles:

### 1. 🌍 Awareness

Users should understand how everyday activities contribute to their estimated carbon footprint.

### 2. 📊 Feedback

Users should immediately see the effect of their environmental choices through calculations and Eco Twin feedback.

### 3. 🌱 Motivation

Sustainability should feel like a continuous journey rather than a one-time calculation.

That is why the application combines:

**Carbon Tracking + Analytics + Gamification + Eco Actions**

---

## 📌 Key Project Highlights

| 🌍 Sustainability | 📊 Analytics | 🌳 Gamification |
|:---:|:---:|:---:|
| Carbon footprint | Historical data | Eco Twin |
| Regional factors | Monthly statistics | Tree growth |
| Waste tracking | Profile dashboard | Happiness |
| Transport tracking | Category analysis | Eco points |

---

## 📚 Learning Outcomes

This project demonstrates practical experience with:

- **Flask web development**
- **REST-style API endpoints**
- **SQLite database integration**
- **CRUD operations**
- **Jinja2 templating**
- **HTML/CSS/JavaScript integration**
- **External API integration**
- **Browser Geolocation API**
- **Reverse geocoding**
- **Data visualization**
- **Caching**
- **Environmental calculations**
- **Gamification logic**
- **Environment variable management**
- **Git/GitHub project management**

---

## 🤝 Contributing

Contributions and improvements are welcome.

### 1. Fork the Repository

Fork the **EcoSessionTree** repository on GitHub.

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature
```

### 3. Make Your Changes

Implement and test your feature.

### 4. Commit Your Changes

```bash
git add .
git commit -m "Add new sustainability feature"
```

### 5. Push Your Branch

```bash
git push origin feature/your-feature
```

### 6. Open a Pull Request

Describe:

- What changed
- Why it was changed
- How it was tested

---

## 📜 License

No explicit open-source license is currently included in the repository.

Until a license is added, the project should be treated as **all rights reserved**.

---

## 👨‍💻 Author

<div align="center">

### Priyanshu Shekhar

**Final Year BE (CSE) Student**

**Developer · DSA Enthusiast · Frontend Developer · Cloud Learner**

[![GitHub](https://img.shields.io/badge/GitHub-priyanshushe-181717?style=for-the-badge&logo=github)](https://github.com/priyanshushe)

[![EcoSessionTree](https://img.shields.io/badge/EcoSessionTree-Repository-2ea44f?style=for-the-badge&logo=github)](https://github.com/priyanshushe/EcoSessionTree)

</div>

---

<div align="center">

## 🌱 Track your footprint. Improve your habits. Grow your Eco Twin.

**EcoSessionTree — Making sustainability measurable, interactive, and engaging.**

⭐ **If you find this project interesting, consider giving the repository a star!** ⭐

</div>
