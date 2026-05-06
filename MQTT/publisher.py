import paho.mqtt.client as mqtt
import time

def on_publish(client, userdata, result):
	print("conexion exitosa")
	print(f"Client:{client}\nUserdata{userdata}\nResult:{result}")

if __name__ == "__main__":
    broker = "127.0.0.1"
    port = 1883
    topic = "Casa/Sala"
    contador = 0
    cliente = mqtt.Client()
    cliente.on_publish = on_publish
    cliente.connect(broker, port, keepalive=60)
    while True:
        cliente.publish(topic, contador)
        contador += 1
        time.sleep(1)
