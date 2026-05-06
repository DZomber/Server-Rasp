archivo = open('prueba.txt','a') # -> r (read, solo leer el archivo) w -> write, escribir en el archivo, ojo se reescribe el archivo a -> escribe al fial del texto original
archivo.write('soy el nuevo texto')
print(archivo)
archivo.close()

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open('registro.txt','a')
for p in registro_ultima_sesion:
    archivo.writelines(p)