# 🌾 CropSense

**Smart farming made simple. Real-time crop monitoring with Arduino, AI predictions, and a beautiful dashboard.**

<div align="center">

[![Status](https://img.shields.io/badge/status-production%20ready-32CD32?style=flat-square&logo=checkmark)]()
[![License](https://img.shields.io/badge/license-MIT-0066cc?style=flat-square)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square&logo=python)]()
[![Node.js](https://img.shields.io/badge/node.js-18%2B-339933?style=flat-square&logo=node.js)]()
[![Docker](https://img.shields.io/badge/docker-ready-2496ED?style=flat-square&logo=docker)]()

[**Quick Start**](#-get-started-in-5-minutes) • [**Architecture**](#-system-architecture) • [**Hardware**](#-hardware-setup) • [**Troubleshooting**](#-troubleshooting)

</div>

---

## 🎯 What is CropSense?

Monitor your crops **in real-time** with Arduino sensors. CropSense reads temperature, humidity, and soil moisture data directly from your fields and delivers actionable insights through an intelligent dashboard.

> **No cloud dependency.** No complex setup. Just sensors, a PC, and a beautiful interface.

### The Problem We Solve

- ❌ Manual field checks take hours
- ❌ Missed irrigation deadlines kill crops
- ❌ No data on what actually happened
- ❌ Complex farm management systems

### The CropSense Solution

- ✅ **Automated monitoring** every 2 seconds
- ✅ **AI-powered predictions** for irrigation
- ✅ **Beautiful dashboard** with real-time updates
- ✅ **Session-based routing** — switch devices without restarting
- ✅ **Dockerized backend** — one command to start everything

---

## ⚡ Feature Highlights

> [!NOTE]
> All core features are production-ready. See [Feature Matrix](#-feature-highlights-1) below.

<table>
<tr>
<td width="50%">

### 🔴 Real-Time Monitoring
- Temperature tracking (°C)
- Humidity measurements (%)
- Soil moisture analysis (%)
- Live update every 2 seconds
- Historical data retention

</td>
<td width="50%">

### 🤖 ML & Predictions
- Trained irrigation model
- Health score calculations
- Crop stress detection
- Automated alerts
- Recommendation engine

</td>
</tr>
<tr>
<td width="50%">

### 🌐 Multi-Device Support
- Manage unlimited devices
- Switch devices instantly
- Session-based routing
- No terminal restarts
- Per-device dashboards

</td>
<td width="50%">

### 🐳 Production Ready
- Docker containerized
- MongoDB cloud compatible
- Auto-scaling ready
- Secure JWT auth
- CORS enabled

</td>
</tr>
</table>

---

## 🚀 Get Started in 5 Minutes

> [!IMPORTANT]
> **Prerequisites**: Arduino board + sensors, Docker Desktop, Python 3.10+, Git

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/cropsense.git
cd cropsense
```

### 2️⃣ Start Backend Services

```bash
docker compose up --build -d
docker compose ps  # verify running
```

```
NAME              SERVICE           STATUS
cropsense-mongo           mongo             Up 15s
cropsense-backend         flask-backend     Up 12s
cropsense-nginx           nginx             Up 10s
```

### 3️⃣ Start Frontend Dashboard

```bash
cd frontend
npm install
npm run dev
```

🎉 **Dashboard ready**: http://localhost:3000

### 4️⃣ Register Your Account

1. Open http://localhost:3000
2. **Register** with any credentials
3. **5 devices auto-created** (rice, wheat, maize, vegetables, pulses)
4. **Select one device** to mark it active (turns GREEN)

### 5️⃣ Upload Arduino Sketch

| Step | Action |
|------|--------|
| 1 | Connect Arduino via USB |
| 2 | Open `aurdino-setup/arduino_sensor/arduino_sensor.ino` in Arduino IDE |
| 3 | Select Board: "Arduino Uno" |
| 4 | Select Port: "COM3" (or your port) |
| 5 | Click **Upload** |
| 6 | Open Serial Monitor (speed: 9600) |

Expected output:
```
[SENSOR] Temp: 28.5°C | Humidity: 65% | Soil: 45%
[SENSOR] Temp: 28.6°C | Humidity: 65% | Soil: 46%
```

### 6️⃣ Run Serial Bridge

```bash
cd aurdino-setup
pip install -r requirements.txt

# ⚡ Ultra-simple command:
python serial_bridge.py --port COM3
```

✅ **Watch your dashboard update in real-time!**

---

## 🏗️ System Architecture

<div align="center">

![System Architecture Diagram](assets/system_architecture.png)

**CropSense seamlessly connects hardware sensors to a smart dashboard through a robust backend infrastructure.**

</div>

---

## 🔌 Hardware Setup

### Components Required

| Component | Qty | Purpose | Cost |
|-----------|-----|---------|------|
| Arduino Uno/Mega | 1 | Microcontroller | $25-35 |
| DHT11 Sensor | 1 | Temperature & Humidity | $5-10 |
| Soil Moisture Sensor | 1 | Soil water level | $2-5 |
| Jumper Wires | Pack | Connections | $3-5 |
| USB Cable | 1 | Arduino connection | $5-10 |
| Breadboard | 1 | Easy wiring | $3-5 |

### Wiring Diagram

**Hardware Setup Images:**

![Hardware Setup - Part 1](assets/hardware/pic1.jpeg)

![Hardware Setup - Part 2](assets/hardware/pic2.jpeg)

**Sensor Connection Reference:**

```
DHT11 Sensor Connections:
┌─────────┐
│ DHT11   │
├─────────┤
│ VCC → 5V (Arduino 5V pin)
│ GND → GND (Arduino GND pin)
│ OUT → D2 (Arduino Digital Pin 2)
└─────────┘

Soil Moisture Sensor Connections:
┌──────────────┐
│ Soil Sensor  │
├──────────────┤
│ VCC → 5V
│ GND → GND
│ AO → A0 (Arduino Analog Pin 0)
└──────────────┘
```

**Interactive 3D Model:**

View the complete hardware setup in 3D using Tinkercad:
[🔗 CropSense Hardware on Tinkercad](https://www.tinkercad.com/things/lE7gdGxIFpB-assignment?sharecode=VNjDAq8IlB0He1O2NTXDys7m4RLNtvScsxcVnZPSCg8)

### Step-by-Step Hardware Assembly

1. **Power Down Arduino** - Disconnect USB before wiring
2. **Connect DHT11**:
   - VCC → Arduino 5V
   - GND → Arduino GND
   - Data pin → Arduino D2
3. **Connect Soil Sensor**:
   - VCC → Arduino 5V
   - GND → Arduino GND
   - Analog Out → Arduino A0
4. **Verify Connections** - Double-check all wires
5. **Connect USB** - Plug in to power Arduino

### Upload Firmware

1. Open Arduino IDE
2. Open `aurdino-setup/arduino_sensor/arduino_sensor.ino`
3. Select Board: **Arduino Uno** (or your board)
4. Select Port: **COM3** (or your COM port)
5. Click **Upload** button
6. Wait for "Uploading complete ✓"

### Verify Hardware Works

```bash
# Open Arduino Serial Monitor
# Tools → Serial Monitor (Ctrl+Shift+M)
# Set speed: 9600 baud

# You should see readings every 2 seconds:
[SENSOR] Temp: 28.50°C | Humidity: 65.30% | Soil: 45%
[SENSOR] Temp: 28.51°C | Humidity: 65.28% | Soil: 46%
[SENSOR] Temp: 28.49°C | Humidity: 65.32% | Soil: 44%

# If you see this, hardware is working! ✅
```

### Connection Reference Table

<table>
<tr><th>Component</th><th>Arduino Pin</th><th>Pin Type</th></tr>
<tr><td>DHT11 VCC</td><td>5V</td><td>Power</td></tr>
<tr><td>DHT11 GND</td><td>GND</td><td>Ground</td></tr>
<tr><td>DHT11 DATA</td><td>D2</td><td>Digital Input</td></tr>
<tr><td>Soil VCC</td><td>5V</td><td>Power</td></tr>
<tr><td>Soil GND</td><td>GND</td><td>Ground</td></tr>
<tr><td>Soil Analog Out</td><td>A0</td><td>Analog Input</td></tr>
</table>

---

## 🔐 Data Security & Integrity

### Authentication & Access Control

CropSense implements a **multi-layer authentication strategy** to ensure data security and prevent unauthorized access:

#### Layer 1: User Authentication (JWT)
- **Registration & Login**: All users register with email/password
- **JWT Tokens**: Secure token-based authentication for API requests
- **Token Validation**: Every API endpoint (except `/health`) validates JWT before processing
- **Session Tracking**: Each user's session stores their currently active device
- **Token Expiration**: Configurable expiration (default: 24 hours) for security

```http
POST /api/auth/register
{
  "name": "John Farmer",
  "email": "john@farm.com",
  "password": "secure_password"
}

Response: { "token": "eyJ0eXAiOiJKV1QiLCJhbGc..." }
```

#### Layer 2: Device Ownership & Session Isolation
- **Device Ownership**: Devices are tied to specific users (e.g., `user_456_RICE`)
- **Session-Based Routing**: Only the active device receives new sensor readings
- **User Isolation**: Users cannot access other users' devices or data
- **Sensor Data Validation**: Backend validates that requesting user owns the device

```python
# Backend authentication flow
@app.route('/api/sensors/ingest', methods=['POST'])
@jwt_required()
def ingest_sensor_data():
    device_id = request.json.get('device_id')
    user_id = get_jwt_identity()
    
    # Verify user owns this device
    device = db.devices.find_one({
        "device_id": device_id,
        "user_id": user_id
    })
    
    if not device:
        return {"error": "Unauthorized"}, 403
    
    # Check if this is the active device
    active_device = db.user_sessions.find_one({
        "user_id": user_id
    }).get('active_device_id')
    
    # Auto-route to active device if needed
    if device_id != active_device:
        device_id = active_device
    
    # Store reading
    sensor_reading = {
        "device_id": device_id,
        "data": request.json,
        "timestamp": datetime.utcnow()
    }
    db.sensor_readings.insert_one(sensor_reading)
```

#### Layer 3: Serial Bridge Security
- **Credential Storage**: Serial bridge stores credentials locally on the farmer's PC (`~/.bridge_auth`)
- **Local Authentication**: Bridge authenticates with backend using stored credentials
- **No API Keys**: Eliminates risk of key exposure or theft
- **Per-Computer Setup**: Each PC must authenticate separately (prevents credential sharing)

```bash
# First time setup - authenticate with your account
python serial_bridge.py --setup

# After setup, credentials are stored securely
python serial_bridge.py --port COM3

# Bridge fetches active device automatically
[INFO] Authenticating...
[AUTH] Credentials loaded from ~/.bridge_auth
[INFO] Active device: user_456_RICE
[SUCCESS] Connected to COM3 at 9600 baud
```

### Data Integrity Mechanisms

#### 1. **Timestamp Validation**
- Every sensor reading includes server-generated timestamp
- Out-of-order readings are rejected
- Prevents replay attacks and data manipulation

#### 2. **Reading Enrichment & Validation**
- Raw sensor values checked against physical limits
  - Temperature: -40°C to +80°C
  - Humidity: 0-100%
  - Soil Moisture: 0-100%
- Invalid readings logged and rejected
- Device lookup ensures data belongs to valid device

#### 3. **Database Indexing for Data Consistency**
```javascript
// MongoDB indexes ensure data integrity
db.sensor_readings.createIndex({ device_id: 1, timestamp: 1 })
db.user_sessions.createIndex({ user_id: 1 }, { unique: true })
db.devices.createIndex({ device_id: 1, user_id: 1 }, { unique: true })
```

#### 4. **Audit Logging**
- All sensor ingestions logged with:
  - User ID
  - Device ID
  - Timestamp
  - Raw values
  - Health score computed
- Enables traceability and debugging
- Detects anomalies in data patterns

### Data Storage & Privacy

| Aspect | Implementation |
|--------|-----------------|
| **Data Location** | MongoDB (local or Atlas cloud) |
| **Encryption in Transit** | HTTPS/TLS (production) |
| **Encryption at Rest** | MongoDB encryption (production) |
| **Data Retention** | User-configurable (default: 90 days) |
| **Data Export** | Users can export their data anytime |
| **Deletion** | Users can delete device + all readings |
| **GDPR Compliance** | Full data portability & deletion support |

---

## 🔑 Session-Based Multi-Device Routing

CropSense enables **one serial bridge to serve multiple devices** without terminal restarts. Here's how it works:

### Architecture

```
┌──────────────────────────────────────────────────────────┐
│ SERIAL BRIDGE (Runs ONCE)                                │
│ python serial_bridge.py --port COM3                      │
│                                                          │
│ Sends: { device_id: "any_value", temp: 28.5, ... }     │
└──────────┬───────────────────────────────────────────────┘
           │
           ↓
┌──────────────────────────────────────────────────────────┐
│ BACKEND (Smart Routing)                                  │
│                                                          │
│ 1. Check: Is this the active device?                    │
│ 2. If NO → Auto-route to active device                  │
│ 3. Store with correct device_id                         │
└──────────┬───────────────────────────────────────────────┘
           │
           ↓
┌──────────────────────────────────────────────────────────┐
│ FRONTEND DASHBOARD                                       │
│                                                          │
│ ☐ RICE  (select me)                                    │
│ ☑ WHEAT (ACTIVE - GREEN)                               │
│ ☐ MAIZE (select me)                                    │
│                                                          │
│ Shows data from WHEAT automatically ✅                  │
└──────────────────────────────────────────────────────────┘
```

### Flow Example

**Scenario**: Farmer wants to switch from RICE monitoring to WHEAT monitoring

```
Step 1: Terminal (Running)
$ python serial_bridge.py --port COM3
[SUCCESS] Connected to COM3 at 9600 baud
[SERIAL] 🌡 Temp: 28.5°C | 💧 Humidity: 65%
[DATA] {temp: 28.5, humidity: 65, soil: 45, raw: 2800}
[BACKEND] ✓ Ingested

Step 2: Dashboard (Browser)
User clicks WHEAT button
← POST /api/sessions/set-active-device
→ Backend stores: { user_id: 456, active_device_id: "user_456_WHEAT" }

Step 3: Next Sensor Reading
Serial Bridge sends: { device_id: "user_456_RICE", temp: 28.6, ... }
Backend checks: Is user_456_RICE the active device? NO
Backend auto-routes to: user_456_WHEAT (from session)
Data stored in: WHEAT device readings

Step 4: Dashboard Updates
Displays WHEAT sensor data immediately ✅
NO TERMINAL RESTART NEEDED! 🎉
```

### Key Benefits

- ✅ **One terminal command** serves all devices
- ✅ **Device switching** happens in dashboard (no coding)
- ✅ **Instant updates** when user changes device
- ✅ **Farmer-friendly** - no technical knowledge required
- ✅ **Production-ready** - no restart downtime

---

### Authentication
```http
POST /api/auth/register
Content-Type: application/json

{
  "name": "John Farmer",
  "email": "john@farm.com",
  "password": "secure123"
}

Response: { "user_id": "...", "token": "eyJ..." }
```

### Sensor Ingestion (No API Keys!)
```http
POST /api/sensors/ingest
Content-Type: application/json

{
  "device_id": "john_farmer_RICE",
  "temperature": 28.5,
  "humidity": 65.3,
  "soil_moisture": 45.2,
  "raw_soil_score": 520
}

Response: { "health_score": 7.8, "alerts": [] }
```

### Get Predictions
```http
GET /api/predictions/{device_id}
Authorization: Bearer eyJ...

Response: {
  "irrigation_needed": true,
  "health_score": 7.8,
  "recommendations": ["Increase watering frequency"]
}
```

---

## 📊 Complete Data Flow Architecture

<div align="center">

![Data Flow Architecture Diagram](assets/data_flow_architecture.png)

**The complete journey of sensor data from Arduino to your dashboard in real-time.**

</div>

### Health Score Calculation

Every sensor reading gets enriched with a **health score** (0-100):

```python
# Processing: backend/app/services/preprocessing_service.py

# Step 1: Calculate component scores
temp_score = 100 - abs(ideal_temp - actual_temp) * 5.0
humidity_score = 100 - abs(ideal_humidity - actual_humidity) * 1.2  
soil_score = 100 - abs(ideal_soil - actual_soil) * 1.7

# Step 2: Average the scores
health_score = (temp_score + humidity_score + soil_score) / 3

# Step 3: Check for alerts
alerts = []
if temp > 35: alerts.append("temperature_high")
if humidity < 30: alerts.append("humidity_low")
if soil < 25: alerts.append("soil_moisture_critical")

# Example:
# Input:  temp=28.50, humidity=65.30, soil=45.0
# Output: health_score=92.13, alerts=[]
```

### Irrigation Prediction Model

When requested, the backend uses a trained Keras neural network to predict if irrigation is needed:

```python
# Processing: backend/app/services/prediction_service.py

# Step 1: Load trained model
model = load_model("trained_models/irrigation_model.keras")

# Step 2: Prepare input
input_features = [
    temperature,              # 28.50
    humidity,                # 65.30
    soil_moisture_normalized, # 0.45 (0-1 scale)
    crop_type_numeric        # 2 (for wheat)
]

# Step 3: Normalize using fitted scaler
input_scaled = scaler.transform([input_features])

# Step 4: Get prediction
prediction = model.predict(input_scaled)  # Returns 0.0-1.0

# Step 5: Interpret result
irrigation_needed = int(prediction[0][0] > 0.5)
# 1 = Water the crop NOW
# 0 = Current irrigation is sufficient

# Example output:
# {
#   "irrigation_needed": 1,
#   "confidence": 0.87,
#   "recommendation": "Increase watering frequency"
# }
```

---

## 📁 Project Structure

```
cropsense/
├── 📄 README_GITHUB.md          ← You are here!
├── 🐳 docker-compose.yml         ← Start everything
├── ⚙️  .env.example              ← Copy to .env
│
├── 🔧 backend/                   ← Flask API
│   ├── app/
│   │   ├── 🎛️  controllers/       ← API handlers
│   │   ├── ⚙️  services/          ← Business logic
│   │   ├── 🗄️  db/               ← MongoDB
│   │   └── 🔐 middleware/        ← Auth
│   ├── 🤖 trained_models/        ← ML model
│   └── 🐳 Dockerfile
│
├── 💻 frontend/                  ← Next.js Dashboard
│   ├── src/
│   │   ├── app/
│   │   │   ├── 🔓 auth/          ← Login/Register
│   │   │   └── 📊 dashboard/     ← Main UI
│   │   └── 🧩 components/        ← React components
│   └── ⚡ next.config.ts
│
├── 🔌 aurdino-setup/             ← Arduino Bridge
│   ├── serial_bridge.py          ← Main relay
│   ├── arduino_sensor/
│   │   └── arduino_sensor.ino    ← Firmware
│   └── requirements.txt
│
└── 📚 assets/                    ← Images & diagrams
    ├── hardware/                 ← Hardware setup images
    └── ui/                       ← Dashboard screenshots
```

---

## 📊 Dashboard & UI Showcase

Get a glimpse of the CropSense dashboard experience:

| Screenshot | Description |
|------------|-------------|
| ![Dashboard Overview](assets/ui/Screenshot%20(112).png) | Main dashboard with real-time sensor data |
| ![Device Monitoring](assets/ui/Screenshot%20(113).png) | Live monitoring of active device |
| ![Health Metrics](assets/ui/Screenshot%20(114).png) | Health scores and crop conditions |
| ![Analytics View](assets/ui/Screenshot%20(115).png) | Historical data and trends |
| ![Device Selection](assets/ui/Screenshot%20(116).png) | Easy device switching interface |

---

## 🛠️ Troubleshooting

> [!WARNING]
> Most issues are in these 3 areas: Arduino connection, Backend services, Device selection

### Arduino Not Sending Data

| Problem | Cause | Solution |
|---------|-------|----------|
| Serial Monitor blank | Cable issue | Use **data cable**, not charging cable |
| Serial Monitor blank | Wrong board | Select correct board in Arduino IDE |
| Serial Monitor shows errors | Sensor wiring | Double-check DHT11 data pin (D2) |
| Permission denied | COM port in use | Close Arduino IDE or other terminals |

### Backend Connection Failed

| Error | Fix |
|-------|-----|
| `Cannot connect to localhost:5000` | Run `docker compose up -d` and wait 15s |
| `MongoDB connection error` | Check `.env` file, verify `MONGO_URI` |
| `Containers not running` | Run `docker compose logs flask-backend` for details |

### Data Not Appearing on Dashboard

> [!IMPORTANT]
> **#1 Reason**: Device not selected as active in dashboard!

**Checklist**:
- ✅ Is any device showing GREEN on dashboard?
- ✅ Did you run serial bridge?
- ✅ Is backend responding? `curl http://localhost:5000/api/health`
- ✅ Any errors in browser console? (F12 key)

---

## 🚀 Production Deployment

### Docker Hub Deployment

```bash
# Build image
docker build -t yourusername/cropsense-backend backend/

# Push to Docker Hub
docker push yourusername/cropsense-backend

# Deploy with production compose file
docker compose -f docker-compose.prod.yml up -d
```

### Environment Configuration

Create `.env` file:

```env
# ⚙️ Flask
FLASK_ENV=production
SECRET_KEY=generate-with-openssl-rand-hex-32
JWT_EXP_HOURS=24

# 🗄️ MongoDB (use Atlas for production)
MONGO_URI=mongodb+srv://user:password@cluster.mongodb.net/
MONGO_DB_NAME=cropsense_db

# 💾 Storage
UPLOAD_DIR=/app/uploads

# 🤖 ML Model
MODEL_PATH=/app/trained_models/irrigation_model.keras
```

### Security Checklist

- [ ] Enable HTTPS with Let's Encrypt
- [ ] Set up MongoDB authentication
- [ ] Use strong `SECRET_KEY` (generate with: `openssl rand -hex 32`)
- [ ] Enable rate limiting on `/api/sensors/ingest`
- [ ] Rotate JWT secrets monthly
- [ ] Set up automated backups
- [ ] Monitor database size
- [ ] Enable logging and monitoring
- [ ] Firewall: Only expose ports 80, 443

---

## 📚 Complete Documentation in README

All documentation is consolidated in this README.md:

| Section | Coverage |
|---------|----------|
| **Quick Start** | Get running in 5 minutes |
| **System Architecture** | System design & components |
| **Hardware Setup** | Wiring diagrams & sensor connections |
| **Data Security & Integrity** | Authentication & data protection |
| **Session-Based Routing** | Multi-device switching |
| **Complete Data Flow** | End-to-end data architecture |
| **API Quick Reference** | Key endpoints & examples |
| **Troubleshooting** | Common issues & solutions |
| **Production Deployment** | Deploy to cloud |
| **Contributing** | Development setup |

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

```bash
# 1. Fork the repository
# 2. Create feature branch
git checkout -b feature/your-amazing-feature

# 3. Make changes and commit
git commit -m "Add: your amazing feature"

# 4. Push to your fork
git push origin feature/your-amazing-feature

# 5. Open Pull Request on GitHub
```

### Development Setup

```bash
# Backend development
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Frontend development
cd frontend
npm install
npm run dev
```

---

## 📄 License

MIT License © 2024 CropSense

See [LICENSE](LICENSE) file for details.

---

## 🙋 Support

Got questions? Check these resources:

- 📖 [**This README**](#-complete-documentation-in-readme) — All documentation here
- 🐛 [**Issues**](https://github.com/yourusername/cropsense/issues) — Report bugs
- 💬 [**Discussions**](https://github.com/yourusername/cropsense/discussions) — Ask questions

---

## 🎉 What's Next?

After your first harvest with CropSense:

1. **Train custom model** with your crop data
2. **Set SMS alerts** for critical conditions
3. **Export data** to CSV for analysis
4. **Deploy to AWS** or DigitalOcean
5. **Build mobile app** with React Native

---

<div align="center">

**Built with ❤️ for sustainable farming.**

[⬆ Back to Top](#-cropsense)

</div>
