import threading
import time

def cuenta(num):
    for i in range(1, num+1):
        print(i)
        time.sleep(1)

if __name__ == "__main__":
    for _ in range(3):
        x = threading.Thread(target=cuenta, args=(5,))
        x.start() 
    print(f"Hilos activos: {threading.active_count()}")
    print("Fin del Programa :D")
    
