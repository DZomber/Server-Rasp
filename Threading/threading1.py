import threading
import time

def funcion(nombre):
    print(f"{nombre} esta dormiendo...")
    time.sleep(1)
    print("Ahora son las 3 AM....")
    time.sleep(1)
    print(f"Ahora {nombre}")

if __name__ == "__main__":
    nuevo_hilo = threading.Thread(target = funcion, args=("Juan",))
    nuevo_hilo.start()

    print(f"Hilos activos: {threading.active_count()}")
    time.sleep(1)
    print("Este es el final de mi programa")
