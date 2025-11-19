# Eco Twin - Carbon Footprint Calculator

## Overview

Eco Twin is a location-aware carbon footprint calculator web application that helps users track and reduce their environmental impact. The application calculates carbon emissions based on user activities (electricity usage, transportation, industrial processes, waste, and events) using GPS location data to provide region-specific emission factors. It features an engaging gamification system with an evolving "Eco Twin" avatar and tree growth visualization that responds to user's environmental performance, along with personalized eco-friendly suggestions based on calculated footprint levels.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Technology Stack**: Traditional server-side rendered HTML templates using Jinja2 templating engine with vanilla JavaScript for client-side interactivity.

**Design Pattern**: Multi-page application (MPA) with four main pages:
- Home: Landing page with feature highlights
- Calculator: Carbon footprint calculation interface with dual input modes (Question Mode and Number Mode)
- Profile: User dashboard with gamification elements (Eco Twin avatar, tree growth visualization, statistics charts)
- Suggestions: Context-aware eco-friendly tips based on footprint category

**UI Framework**: Custom CSS using a soft pastel color theme with CSS variables for consistent styling. Implements glassmorphism effects and smooth animations.

**Key Frontend Libraries**:
- Leaflet.js (v1.9.4): Interactive map visualization for GPS location display
- Chart.js: Data visualization for carbon footprint statistics and trends
- Native Geolocation API: GPS coordinates acquisition

**Rationale**: Server-side rendering chosen for simplicity and better initial page load performance. Vanilla JavaScript minimizes dependency overhead while maintaining sufficient interactivity for the application's needs.

### Backend Architecture

**Framework**: Flask (Python web framework)

**Architecture Pattern**: Monolithic application with route-based page serving and RESTful API endpoints for AJAX requests.

**Session Management**: Flask's built-in session system with server-side sessions stored using secure cookies. Session secret key required via environment variable for security.

**Calculation Engine**: Pure Python implementation using comprehensive emission factor lookup tables:
- State-specific electricity emission factors (kg CO₂/kWh) for Indian states and US states
- Vehicle-type emission factors based on fuel type and efficiency
- Industrial process emission factors
- Waste disposal emission factors

**Caching Strategy**: In-memory dictionary-based API response caching with 5-minute TTL to minimize external API calls and improve performance.

**Logging**: Python's built-in logging module for error tracking and debugging.

**Rationale**: Flask chosen for lightweight footprint and rapid development. Monolithic architecture appropriate for application scale. In-memory caching sufficient for current scale (would need Redis/Memcached for production scaling).

### Data Storage

**Database**: SQLite3 (file-based relational database)

**Schema Design**: User session-based data storage with tables for:
- Calculation history with timestamps
- Location data (latitude, longitude, city, state)
- Emission calculations by category
- User progress metrics (tree level, eco twin stage)

**Data Persistence**: Server-side session storage for user state management across requests. Calculation history persisted to SQLite for trend analysis and profile statistics.

**Rationale**: SQLite chosen for simplicity, zero-configuration setup, and sufficient performance for single-user or small-scale deployments. File-based storage eliminates need for separate database server. Migration path to PostgreSQL available if multi-user scaling required.

### Authentication & Authorization

**Current Implementation**: Session-based user tracking without traditional authentication. Users identified by session ID.

**Security Measures**:
- Secure session cookies with cryptographic signing using SESSION_SECRET
- Environment variable validation on startup
- No sensitive user data collection (privacy-first approach)

**Rationale**: Simplified authentication appropriate for single-user deployment and privacy-focused design. Session-only approach reduces barrier to entry while maintaining user progress tracking.

## External Dependencies

### Required Environment Variables
- `SESSION_SECRET`: Cryptographic key for session cookie signing (required, application exits if not set)
- `OPENWEATHER_API_KEY`: OpenWeather API key for weather and air quality data (optional, graceful degradation if missing)

### Third-Party APIs

**OpenWeather API**:
- **Purpose**: Reverse geocoding (coordinates to city/state), current weather conditions, air quality index (AQI)
- **Endpoints Used**: 
  - Geocoding API for location resolution
  - Current Weather API for temperature and conditions
  - Air Pollution API for AQI data
- **Fallback**: Application continues functioning without API; shows "unavailable" for weather/AQI data
- **Rate Limiting**: Mitigated through 5-minute response caching

### External Libraries (CDN-delivered)

**Leaflet.js (v1.9.4)**:
- **Purpose**: Interactive map rendering and GPS location visualization
- **Source**: unpkg.com CDN
- **Rationale**: Lightweight, open-source alternative to Google Maps

**Chart.js**:
- **Purpose**: Carbon footprint trend visualization and statistics charts
- **Source**: jsdelivr.net CDN
- **Rationale**: Simple API, responsive charts, no configuration overhead

### Python Dependencies
- Flask: Web framework
- requests: HTTP client for API calls
- python-dotenv: Environment variable management
- sqlite3: Built-in database interface (no external installation)

### Emission Factor Data Sources
- US EPA 2023 data for state-specific electricity grid intensities
- Industry-standard vehicle emission factors
- Referenced within application code as lookup tables (no external API dependency)