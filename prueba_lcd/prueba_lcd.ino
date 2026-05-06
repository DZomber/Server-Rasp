#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

// ==========================================
// LCD CONFIG
// ==========================================
LiquidCrystal_I2C lcd(0x27, 16, 2);

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

const char* device_id = "ESP_lcd";

const char* topic_command   = "Cuarto/Led/cmd";
const char* topic_telemetry = "Cuarto/Led/data";
const char* topic_status    = "Cuarto/Led/status";

// ==========================================
WiFiClient espClient;
PubSubClient client(espClient);



// ==========================================
// VARIABLES DE ESTADO
// ==========================================
String estadoWiFi = "OFF";
String estadoMQTT = "OFF";
String estadoLuz  = "OFF";

// ==========================================
// FUNCION LCD (SIN PARPADEO)
// ==========================================
void actualizarLCD() {
  lcd.setCursor(0,0);
  lcd.print("WiFi:");
  lcd.print(estadoWiFi);
  lcd.print(" MQTT:");
  lcd.print(estadoMQTT);
  lcd.print("   "); // limpia sobra

  lcd.setCursor(0,1);
  lcd.print("Light:");
  lcd.print(estadoLuz);
  lcd.print("        ");
}

// ==========================================
// WIFI
// ==========================================
void setup_wifi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Connecting WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  estadoWiFi = "OK";
  actualizarLCD();
}

// ==========================================
// CALLBACK MQTT
// ==========================================
void callback(char* topic, byte* payload, unsigned int length) {

  String message;
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }

  Serial.print("Mensaje recibido: ");
  Serial.println(message);

  if (String(topic) == topic_telemetry) {

    if (message.indexOf("ON") != -1) {
      estadoLuz = "ON";
    }

    else if (message.indexOf("OFF") != -1) {
      estadoLuz = "OFF";
    }

    actualizarLCD();
  }
}

// ==========================================
// RECONNECT MQTT
// ==========================================
void reconnect() {
  while (!client.connected()) {

    estadoMQTT = "CONN";
    actualizarLCD();

    if (client.connect(device_id, NULL, NULL, topic_status, 1, true, "offline")) {

      estadoMQTT = "OK";
      client.publish(topic_status, "online", true);
      client.subscribe(topic_telemetry);

    } else {
      estadoMQTT = "FAIL";
      actualizarLCD();
      delay(3000);
    }
  }
}

// ==========================================
// SETUP
// ==========================================
void setup() {
  Serial.begin(115200);

 

  lcd.init();
  lcd.backlight();

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