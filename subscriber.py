import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
	print(f"Conectado con el codigo {rc}")
	if rc ==0:
		print("Conexion exitosa")
	else:
		print("Fallo en la conexion")

def on_message(client, userdata, message):
	print(f"Mensaje recibido: {message.payload.decode()}")
	print(f"Nombre del topic {message.topic}")

if __name__  == "__main__":
	broker = "localhost" #192.168.1.x -> Direccion IP de la raspberry
	port = 1883
	topic = "Casa/Sala"
	
	cliente = mqtt.Client()
	cliente.on_connect = on_connect
	cliente.on_message = on_message
	
	cliente.connect(broker, port, keepalive =60)
	
	cliente.subscribe(topic)
	"""
	1. Simple string y un int:
	subscribe("my/topc",0)
	2. Una tupla con el topic y el qos:
	subscribe(("my/topic",1))
	3. Una lista de tuplas con varias topics
	subscribe([("my/topic",0),("other topic",1)..])
	"""
	cliente.loop_forever()

	
