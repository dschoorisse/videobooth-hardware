# ESP32 Photobooth Hub

ESPHome-based central controller for a photobooth system handling lighting, hardware shutdown, and system integration.

## Hardware

- **Board:** M5Stack Atom (ESP32)
- **LEDs:** 2x SK6812 strips (1 LED each)
  - GPIO26: Printer status LED
  - GPIO27: Front lighting LED
- **Button:** GPIO21 - Physical shutdown button (connects to GND, internal pullup enabled)

## Features

### LED Control
- **Printer LED (GPIO26):** Status indication with multiple states
  - Standby: Orange glow
  - Printing: Fast red pulse
  - Finished: Slow green pulse
  - Off: LED disabled

- **Front LED (GPIO27):** Subject lighting
  - Standby: Dim white
  - Active: Full brightness white
  - Off: LED disabled

### Hardware Shutdown Button
- Hold button for 5+ seconds to trigger shutdown
- Sends MQTT command to `lights/shutdown/command`
- JSON payload includes command, reason, uptime, and request ID

## MQTT Topics

### Incoming Commands
- `lights/printer/command` - Controls printer status LED
  - `STANDBY`, `PRINTING`, `FINISHED`, `OFF`
- `lights/front/command` - Controls front lighting
  - `STANDBY`, `ACTIVE`

### Outgoing Commands
- `lights/shutdown/command` - Hardware shutdown request
- `lights/status` - Device online/offline status

## Configuration

Static IP: `192.168.2.54`
MQTT Broker: `192.168.1.3:1883`

WiFi credentials and MQTT authentication stored in `secrets.yaml`:
```yaml
wifi_ssid: "your_network"
wifi_password: "your_password"
mqtt_videobooth_username: "username"
mqtt_videobooth_password: "password"
```

## Installation

1. Install [ESPHome](https://esphome.io/)
2. Create `secrets.yaml` with WiFi and MQTT credentials
3. Flash with: `esphome run PhotoboothHub.yaml`

## Future Enhancements

- DMX lighting control integration
- Additional sensor inputs
- Extended system monitoring