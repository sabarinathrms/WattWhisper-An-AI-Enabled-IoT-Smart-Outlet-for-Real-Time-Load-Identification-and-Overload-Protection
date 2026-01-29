# 🔌 WattWhisper
### AI-Enabled IoT Smart Outlet for Real-Time Load Identification and Overload Protection

WattWhisper is an AI-powered smart outlet that integrates Internet of Things (IoT) and Machine Learning (ML) to monitor power consumption, identify connected electrical appliances, and automatically protect circuits from overload conditions.

---

## 📌 Problem Statement
Traditional smart plugs only measure energy usage and rely on fixed thresholds for overload protection. They cannot identify connected appliances or adapt to dynamic electrical behavior, which can lead to energy wastage and unsafe operating conditions.

---

## 💡 Proposed Solution
WattWhisper combines real-time electrical sensing with AI-based current signature analysis to provide intelligent energy management. The system continuously monitors voltage, current, and power, identifies appliances, and disconnects the load automatically during unsafe conditions.

---

## 🚀 Key Features
- Real-time voltage, current, and power monitoring
- Appliance identification using AI
- Automatic overload detection and relay-based protection
- Remote monitoring and manual control via Blynk dashboard
- Low-cost, scalable, and modular design

---

## 🧠 System Architecture
1. INA219 sensor measures voltage and current
2. ESP8266 NodeMCU processes and transmits data
3. Cloud-based AI analyzes current signatures
4. Blynk IoT platform displays data and sends alerts
5. Relay module disconnects load during overload

---

## 🛠 Hardware Components
- ESP8266 NodeMCU  
- INA219 Current & Voltage Sensor  
- Relay Module (HL-52S)  
- LED Load  
- DC Motor Fan  
- LM2596 Buck Converter  
- Breadboard & Jumper Wires  

---

## 💻 Software & Tools
- Arduino IDE  
- Google Colab (AI Model)  
- Blynk IoT Platform  

---

## 📊 Experimental Results
- Appliance identification accuracy: ~95%
- Overload detection and response time: ~1.1 seconds
- Reliable operation for low and medium power loads

---

## 📱 Blynk Dashboard
- Displays real-time voltage, current, and power
- Shows identified appliance type
- Sends instant overload alerts
- Allows remote ON/OFF control of loads

---

## 🔒 Safety Mechanism
The relay module acts as a hardware-level protection unit. When abnormal current is detected, the AI triggers the ESP8266 to disconnect the load instantly, preventing overheating, short circuits, and equipment damage.

---

## 📈 Limitations
- Tested with limited appliance types
- Cloud dependency for AI processing
- Performance may vary for complex nonlinear loads

---

## 🔮 Future Enhancements
- Support for multiple appliances
- Edge AI integration
- Predictive energy analytics
- Smart grid integration

---

## 📄 Research Paper
**WattWhisper: An AI-Enabled IoT Platform for Real-Time Electrical Load Identification and Overload Protection**

---

## 👤 Author
**Sabarinath S**  
Department of Electronics and Communication Engineering  
M. Kumarasamy College of Engineering  

---

## 📜 License
This project is licensed under the **MIT License**.
