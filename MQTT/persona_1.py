import paho.mqtt.client as mqtt
import time


FLAG= True 

def on_connect(client, userdata, flags, rc):
	print(f"Conectado --- Codigo: {rc}")

def on_message(client, userdata, message):
	global FLAG
	global mensaje
	respuesta = message.payload.decode()
	print(f"respuesta:{respuesta}")
	if respuesta == "salir":
		FLAG = False
	else:
		mensaje = input("Introduce un mensaje: ")
		mensaje = mensaje.lower()
		client.publish(topic_publisher, mensaje)

def on_subscribe(client, userdata, mid, granted_qos):
	print("Suscrito con exito:")

def on_unsubscribe(client, userdata, mid, granted_qos):
	print("Has eliminado la suscripcion")


def on_disconnect(client, userdata, rc):
	if rc !=0:
		print("Ha ocurrido una conexion inesperada")


if __name__== "__main__":
	broker = "127.0.0.1" #mqtt.eclipse.org
	port= 1883
	topic_publisher ="Chat/Cliente1"
	topic_subscriber ="Chat/Cliente2"
	
	cliente = mqtt.Client()
	cliente.on_connect =on_connect
	cliente.on_subscribe = on_subscribe
	cliente.on_unsubscribe = on_unsubscribe
	cliente.on_message = on_message

	cliente.connect(broker, port, keepalive=60)
	time.sleep(1)
	
	cliente.loop_start()
	cliente.subscribe(topic_subscriber)
	time.sleep(1)
	mensaje = input("Introduce un mensaje: ")
	mensaje = mensaje.lower()
	cliente.publish(topic_publisher, mensaje)

	while True:
    		if (FLAG == False) or (mensaje == "salir"):
        		break
    		time.sleep(0.5)

	cliente.loop_stop()
	cliente.disconnect()
