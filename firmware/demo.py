import requests, time

# --- Blynk configuration ---
BLYNK_AUTH = "iTBL5c-Yustkubx9rXsN2EBxVZhENyOS"
BLYNK_URL = "https://blynk.cloud/external/api"

# --- Device current profiles (Amps) ---
device_profiles = {
    'LED': 0.05,       # LED typical
    'MotorFan': 0.80   # Fan normal current
}

NO_DEVICE_THRESHOLD = 0.01  # below this → no load

def read_blynk(pin):
    """Read numeric value from a Blynk virtual pin"""
    try:
        r = requests.get(f"{BLYNK_URL}/get?token={BLYNK_AUTH}&{pin}")
        if r.status_code == 200:
            data = r.json()
            val = float(data[0]) if isinstance(data, list) else float(data)
            return val
        else:
            print("Read error:", r.status_code, r.text)
    except Exception as e:
        print("Error reading:", e)
    return None

def write_blynk(pin, value):
    """Write a value (text or numeric) to a Blynk virtual pin"""
    try:
        requests.get(f"{BLYNK_URL}/update?token={BLYNK_AUTH}&{pin}={value}")
    except Exception as e:
        print("Write error:", e)

def classify_device(current):
    """Identify device type and detect overload"""
    if current < NO_DEVICE_THRESHOLD:
        return "No Device", 0

    # Closest device profile
    device = min(device_profiles, key=lambda k: abs(device_profiles[k] - current))

    # Overload logic
    if device == "MotorFan":
        overload = 1 if current > 0.78 else 0   # <-- Changed threshold to 0.78 A
    elif device == "LED":
        overload = 1 if current > 0.1 else 0
    else:
        overload = 0

    return device, overload

print("⚙ WattWhisper AI model started (REST API mode)...\n")

while True:
    current = read_blynk("V7")
    if current is not None:
        device, overload = classify_device(current)
        print(f"⚡ Current={current:.3f} A | Device={device} | Overload={overload}")

        # Send status to Blynk dashboard
        write_blynk("V6", device)
        write_blynk("V5", overload)

        # --- Auto OFF logic ---
        if overload == 1 and device == "MotorFan":
            print("⚠ Overload detected (> 0.78 A) – Turning OFF relay.")  # updated print
            write_blynk("V1", 0)  # OFF relay on ESP8266
            time.sleep(5)         # give time before next check
        else:
            time.sleep(2)

    else:
        print("⚠ No data from Blynk (V7 missing updates).")
        time.sleep(2)