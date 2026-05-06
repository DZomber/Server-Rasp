import os
'''
ruta = os.getcwd()
print(ruta)
ruta = os.makedirs('C:\\Users\\Zomber\\Desktop\\Alternativo\\Otra')
print(ruta)
archivo = open('Otro_archivo.txt')
print(archivo.read())
archivo.close()
'''
ruta2 = 'C:\\Users\\Zomber\\Documents\\Curso Udemy\\PYTHON\\Python\\Day_6\\prueba.txt'
elemento = os.path.basename(ruta2)
print(f'basename{elemento}')
elemento2 = os.path.dirname(ruta2)
print(elemento2)
elemento3 = os.path.split(ruta2)
print(elemento3)

#os.rmdir('C:\\Users\\Zomber\\Desktop\\Alternativo\\Otra')
otro_archivo = open('C:\\Users\\Zomber\\Desktop\\Alternativo\\Otro_archivo.txt')
print(otro_archivo.read())
otro_archivo.close()