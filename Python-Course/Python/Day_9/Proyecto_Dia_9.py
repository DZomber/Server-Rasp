#import shutil
#shutil.unpack_archive('Proyecto+Dia+9.zip','Proyecto+Dia+9')
#leer_instrucciones = open('C:\\Users\\Zomber\\Documents\\Curso Udemy\\PYTHON\\Python\\Day_9\\Proyecto+Dia+9\\Instrucciones.txt').read()
#print(leer_instrucciones)

import os
import re
import datetime
import time
import math
inicio = time.time()
bt= []
ct =[]
conta = 0
carpeta = 'C:\\Users\\Zomber\\Documents\\Curso Udemy\\PYTHON\\Python\\Day_9\\Proyecto+Dia+9\\Mi_Gran_Directorio'

for ruta, directorio,archivo in os.walk(carpeta):


    for archivo in archivo:


        a = open(os.path.join(ruta, archivo), 'r').read()
        patron = r"N[a-zA-Z]{3}-\d{5}"

        chequear = re.search(patron, a)


        if chequear:
            conta = conta + 1
            bt.append(archivo)
            ct.append(chequear.group())
final =time.time()
fecha = datetime.date.today()
print(f'Fecha de busqueda {fecha}')
print(f'ARCHIVO   \t\t\t   Nro de SERIES\n{'-  ' * 4}            {'-  ' * 4}')
for i, j in zip(bt,ct):
    print(f'{i} \t\t\t {j}')
print('Numeros encontrados:', conta)
print('Duracion de busqueda:´',math.ceil(final-inicio))