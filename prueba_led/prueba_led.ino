#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h> 

// ==========================================
// WIFI + MQTT CONFIG
// ==========================================
//const char* ssid = "Sist.Int_B1AC_2.4";
//const char* password = "R2ycHNATmP";
const char* ssid = "INFINITUM609C";
const char* password = "cRTVk4B2Hy";

//const char* mqtt_server = "192.168.1.210";
const char* mqtt_server = "192.168.1.92";
const int mqtt_port = 1883;

const char* device_id = "ESP_led";

const char* topic_command   = "Cuarto/Led/cmd";
const char* topic_telemetry = "Cuarto/Led/data";
const char* topic_status    = "Cuarto/Led/status";

// ==========================================
WiFiClient espClient;
PubSubClient client(espClient);

#define LED_PIN 2


// ==========================================
// WIFI
// ==========================================
void setup_wifi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);


  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

}

// ==========================================
// CALLBACK MQTT
// ==========================================
void callback(char* topic, byte* payload, unsigned int length) {

  String message;
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }

  Serial.print("Mensaje: ");
  Serial.println(message);

  if (String(topic) == topic_command) {

    if (message == "ON") {
      digitalWrite(LED_PIN, HIGH);
      client.publish(topic_telemetry, "{\"Led\":\"ON\"}");
      
      
    }

    else if (message == "OFF") {
      digitalWrite(LED_PIN, LOW);
      client.publish(topic_telemetry, "{\"Led\":\"OFF\"}");
      
    }
  }
}

// ==========================================
// RECONNECT MQTT
// ==========================================
void reconnect() {
  while (!client.connected()) {


    if (client.connect(device_id, NULL, NULL, topic_status, 1, true, "offline")) {

      
      client.publish(topic_status, "online", true);
      client.subscribe(topic_command);

    } else {

      delay(3000);
    }
  }
}

// ==========================================
// SETUP
// ==========================================
void setup() {
  Serial.begin(115200);

  pinMode(LED_PIN, OUTPUT);

  setup_wifi();

  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);
}

// ==========================================
// LOOP
// ==========================================
void loop() {

  if (!client.connected()) {
    reconnect();
  }

  client.loop();
}
