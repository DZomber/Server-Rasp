import threading
import time

mi_lista =[]

def cuenta(num):
    for i in range(1, num+1):
        mi_lista.append(i)
        time.sleep(0.2)

if __name__ == "__main__":
    hilo_1 = threading.Thread(target=cuenta, args=(5,))
    hilo_1.start()
    hilo_2 = threading.Thread(target=cuenta, args=(5,))
    hilo_2.start()

    hilo_1.join()
    hilo_2.join()
    print(mi_lista)
    
