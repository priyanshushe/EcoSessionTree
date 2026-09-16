<div align="center">

# 🌱 EcoSessionTree

### Turn everyday activities into a measurable carbon footprint — and grow your Eco Twin.

A location-aware Flask web application that estimates monthly **CO₂ emissions**, visualizes environmental impact, and uses **gamification** to encourage more sustainable choices.

<br>

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-F7DF1E?logo=javascript&logoColor=black)
![Leaflet](https://img.shields.io/badge/Leaflet-Maps-199900?logo=leaflet&logoColor=white)

</div>

---

## 📌 Table of Contents

- [🌍 Overview](#-overview)
- [✨ Features](#-features)
- [🔄 How It Works](#-how-it-works)
- [🧮 Carbon Calculation](#-carbon-calculation)
- [🌳 Gamification](#-gamification)
- [🛠️ Technology Stack](#️-technology-stack)
- [🏗️ Application Architecture](#️-application-architecture)
- [📁 Project Structure](#-project-structure)
- [🌐 Application Routes](#-application-routes)
- [🔌 API Reference](#-api-reference)
- [🗄️ Database Design](#️-database-design)
- [🌐 External Services](#-external-services)
- [🔐 Environment Variables](#-environment-variables)
- [🚀 Installation](#-installation)
- [▶️ Running on Replit](#️-running-on-replit)
- [🔒 Security](#-security)
- [⚠️ Limitations](#️-limitations)
- [🚀 Future Enhancements](#-future-enhancements)
- [📄 License](#-license)

---

## 🌍 Overview

**EcoSessionTree** is a sustainability-focused web application designed to help users understand the environmental impact of their everyday activities.

The application estimates monthly carbon emissions across four major areas:

- ⚡ **Electricity**
- 🚗 **Transport**
- 🏭 **Industries / Consumption**
- 🗑️ **Waste**

Users can calculate their footprint in two ways:

1. **Question Mode** — answer simple lifestyle-based questions.
2. **Number Mode** — enter numerical monthly consumption values.

The application calculates the estimated footprint in **kg CO₂/month**, classifies the result as **Low, Medium, or High**, stores the calculation in SQLite, and updates the user's **Eco Twin** progression.

> **EcoSessionTree combines carbon tracking, location awareness, environmental information, analytics, and gamification into one interactive web application.**

---

## ✨ Features

### 🌱 Carbon Footprint Calculator

- Calculates estimated monthly CO₂ emissions.
- Displays annual carbon emissions in tonnes.
- Provides category-wise emission breakdown.
- Classifies the footprint as **Low**, **Medium**, or **High**.
- Stores calculation history.
- Supports both qualitative and numerical inputs.

### ❓ Question Mode

Question Mode is designed for users who do not know their exact monthly consumption.

Users provide lifestyle-based answers for:

- Electricity usage
- Transportation
- Industries / consumption
- Waste generation

The application converts these selections into predefined emission estimates.

### 🔢 Number Mode

Number Mode allows users to enter approximate monthly values directly.

Supported inputs include:

- Electricity — **kWh/month**
- Transport — **km/month**
- Industries / consumption — **kg CO₂/month**
- Waste — **kg/month**

### 📍 Location Awareness

The application uses the browser's **Geolocation API** to obtain the user's latitude and longitude.

Location information is used for:

- Reverse geocoding
- Regional electricity emission factors
- Map visualization
- Weather information
- Air-quality information

### 🗺️ Interactive Map

The application uses **Leaflet.js** and **OpenStreetMap** to display the detected location.

### 🌤️ Weather & Air Quality

When an OpenWeather API key is configured, the application can retrieve:

- Temperature
- Weather description
- Humidity
- Wind speed
- Air Quality Index

Fallback values are available when the API key is not configured.

### 📊 Profile Dashboard

The profile dashboard provides:

- Total points
- Eco Twin happiness
- Total calculations
- Tree level
- Tree stage
- Latest footprint category
- Monthly emissions
- Category-wise emissions
- Historical footprint chart
- Recent calculation history

### 🌳 Gamification

EcoSessionTree uses an Eco Twin progression system.

Users can:

- Earn points by saving calculations.
- Earn additional points by completing eco-actions.
- Increase Eco Twin happiness.
- Progress through tree stages.
- Advance the tree level through sustainable behaviour.
- Experience tree-stage changes based on footprint category.

### 💡 Eco Suggestions

The application provides sustainability suggestions covering:

- Electricity
- Transportation
- Industries / consumption
- Waste

Users can complete recommended actions to earn points.

### 🌿 Eco Events & Workshops

The application provides sustainability-related event and workshop information based on environmental categories.

### 📈 Calculation History

The application stores historical footprint calculations including:

- Total CO₂
- Footprint category
- Calculation timestamp
- Location
- Latitude
- Longitude
- City
- State
- Input mode
- Category-wise emissions

---

## 🔄 How It Works

```text
                    ┌──────────────────────┐
                    │        User          │
                    │                      │
                    │  Opens EcoSessionTree │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Calculator       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Browser Geolocation  │
                    │ Latitude + Longitude  │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
       Reverse Geocode     Weather/AQI      Map Display
             │                 │                 │
             └─────────────────┼─────────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Select Input Mode    │
                    │                      │
                    │ Question / Number    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Carbon Calculation   │
                    │                      │
                    │ Electricity          │
                    │ Transport            │
                    │ Industries           │
                    │ Waste                │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Footprint Result     │
                    │                      │
                    │ kg CO₂ / month       │
                    │ Low / Medium / High  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     SQLite DB        │
                    │                      │
                    │ Save calculation     │
                    │ Update user stats    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Profile Dashboard  │
                    │                      │
                    │ History + Charts     │
                    │ Eco Twin + Progress  │
                    └──────────────────────┘
