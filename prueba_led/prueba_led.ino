#include <WiFi.h>
#include <PubSubClient.h>


// ==========================================
// 1. CONFIGURATION (Edit these)
// ==========================================
const char* ssid = "Sist.Int_B1AC_2.4";
const char* password = "R2ycHNATmP";

// MQTT Broker Settings (Using public HiveMQ for demo, change for production)
const char* mqtt_server = "192.168.1.210";
const int mqtt_port = 1883; 
const char* mqtt_user = ""; // Leave blank for public brokers
const char* mqtt_pass = "";

// Unique Device ID (Must be unique on the broker)
const char* device_id = "ESP_prueba"; 

// Topics (Structure: device_type/device_id/function)
const char* topic_telemetry = "Cuarto/Led/data";   // Where we send sensor data
const char* topic_command   = "Cuarto/Led/cmd";    // Where we listen for commands
const char* topic_status    = "Cuarto/Led/status"; // LWT (Online/Offline)

// ==========================================
// 2. GLOBAL OBJECTS & VARIABLES
// ==========================================
WiFiClient espClient;
PubSubClient client(espClient);

// Timers for non-blocking delays
unsigned long lastMsgTime = 0;
const long interval = 5000; // Send data every 5 seconds

#define LED_PIN 2 // Onboard LED

// ==========================================
// 3. SETUP WIFI
// ==========================================
void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to WiFi: ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

// ==========================================
// 4. CALLBACK (Handle Incoming Messages)
// ==========================================
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");

  // Convert payload to string for easier handling
  String message;
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  Serial.println(message);

  // -- Command Logic --
  // Example: If we receive "ON", turn on LED
  if (String(topic) == topic_command) {
    if (message == "ON") {
      digitalWrite(LED_PIN, HIGH);
      // Feedback: Publish new state immediately
      client.publish(topic_telemetry, "{\"Led\": \"ON\"}"); 
    } else if (message == "OFF") {
      digitalWrite(LED_PIN, LOW);
      client.publish(topic_telemetry, "{\"Led\": \"OFF\"}");
    }
  }
}

// ==========================================
// 5. RECONNECT (The Engine Room)
// ==========================================
void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    
    // --- LWT CONFIGURATION ---
    // define Last Will: Topic, QoS, Retain, Message
    // If this ESP32 dies, the Broker will post "offline" to the status topic automatically.
    
    if (client.connect(device_id, mqtt_user, mqtt_pass, topic_status, 1, true, "offline")) {
      Serial.println("connected");
      
      // Once connected, publish an announcement that we are alive (Retained = true)
      client.publish(topic_status, "online", true);
      
      // Resubscribe to command topics
      client.subscribe(topic_command);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000); // Blocking delay here is acceptable as we can't operate without connection
    }
  }
}

// ==========================================
// 6. MAIN SETUP
// ==========================================
void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  
  setup_wifi();
  
  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);
}

// ==========================================
// 7. MAIN LOOP
// ==========================================
void loop() {
  // Ensure we stay connected
  if (!client.connected()) {
    reconnect();
  }
  client.loop(); // Keep MQTT alive
}
