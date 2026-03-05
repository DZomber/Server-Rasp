import socket

if __name__ == "__main__":
    # 1. Crear socket
    mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    host = socket.gethostbyname(socket.gethostname())
    
    # 2. Conectar con servidor
    mi_socket.connect((host, 1234))
    
    # 3. Enviar request
    mensaje = input("Introduce un mensaje para el servidor: ")
    mi_socket.send(mensaje.encode())
    
    # 4. Recibir response
    datos = mi_socket.recv(1000)
    print("Respuesta del servidor:", datos.decode())
    
    # 5. Cerrar socket
    mi_socket.close()