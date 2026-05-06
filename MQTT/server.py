import socket

if __name__ == "__main__":
    # 1. Crear socket
    mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #servidor = socket.gethostbyname(socket.gethostname())
    servidor = "0.0.0.0"
    
    # 2. Enlazar socket a puerto e IP
    mi_socket.bind((servidor, 1234))
    
    # 3. Escuchar conexión
    mi_socket.listen(1)
    
    print("Servidor esperando conexiones...")

    while True:
        # 4. Aceptar conexión
        conexion, direccion = mi_socket.accept()
        print(f"Conexión aceptada desde {direccion}")
        
        # 5. Recibir request
        datos = conexion.recv(1000)
        print(f"Mensaje recibido: {datos.decode()}")
        
        # 6. Enviar response
        conexion.send("Mensaje recibido correctamente".encode())
        
        # 7. Cerrar conexión
        conexion.close()