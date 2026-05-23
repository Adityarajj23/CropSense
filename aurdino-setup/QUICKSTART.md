# Arduino Connection - Quick Start Guide

## The Big Picture

Your Arduino will:
1. Read temperature, humidity, and soil moisture sensors every 2 seconds.
2. Print the readings over USB serial.
3. A Python bridge on your PC reads the serial output and sends it to the Flask backend.
4. The backend stores the data and computes crop health score and alerts.

```
Arduino sensors -> USB serial -> Python bridge on PC -> Flask backend -> MongoDB
```

## Step 1: Start the backend

From the project root:

```bash
docker compose up --build -d
docker compose ps
```

You should see `mongo` and `flask-backend` running.

## Step 2: Install bridge dependencies

```bash
cd aurdino-setup
pip install -r requirements.txt
```

## Step 3: Upload the Arduino sketch

Open [arduino_sensor/arduino_sensor.ino](arduino_sensor/arduino_sensor.ino).

It already uses:

```cpp
Serial.begin(9600);
```

So the bridge must also use `9600` baud.

Upload the sketch to your Arduino and open Serial Monitor at `9600` baud.

Expected output:

```text
[SENSOR] Temp: 28.0°C | Humidity: 65.0% | Soil: 45%
[RAW] Soil Value: 512
----------------------
```

## Step 4: Register user in frontend (NO TERMINAL NEEDED!)

1. Open browser: http://localhost:3000
2. Click "Register"
3. Fill form:
   - Name: "Farmer John"
   - Email: "john@farm.com"  
   - Password: "secure123"
4. Click Register → Dashboard loads!
   - ✅ You now have 5 devices (rice, wheat, maize, vegetables, pulses)
   - ✅ NO API keys to copy!
   - ✅ Dashboard ready!

## Step 5: Authenticate Serial Bridge (First Time Only)

```bash
cd aurdino-setup
python serial_bridge.py --setup
```

You'll be prompted to enter:
- Email (your dashboard login email)
- Password

This stores your credentials securely on your PC. You only need to do this ONCE!

## Step 6: Select Active Device in Dashboard

1. Open http://localhost:3000
2. Log in with your credentials
3. In dashboard, find your device (Rice, Wheat, etc.)
4. Click to select it (it turns GREEN - this marks it as active)

## Step 7: Run Serial Bridge

Now it's simple - just specify the port:

```bash
python serial_bridge.py --port COM3
```

Or let it auto-detect the port:

```bash
python serial_bridge.py
```

The bridge will:
- ✅ Auto-fetch active device from your dashboard
- ✅ Connect to Arduino on specified port
- ✅ Stream sensor data to the backend
- ✅ Update dashboard in real-time
- ✅ Switch devices anytime → Same bridge, new data! ✨

Done! No config files, no API keys, no complexity! 🚀

## Troubleshooting

- If the bridge cannot see the board, check the COM port in Device Manager
- If the bridge prints parse errors, verify the Arduino sketch prints lines starting with `[SENSOR]`
- If data doesn't appear on dashboard, ensure you selected an active device first
- If `localhost` doesn't work, confirm the backend container is running: `docker compose ps`

## Notes

- No ESP32 is required
- No Wi-Fi is required on the Arduino
- The PC (serial bridge) handles all network communication
