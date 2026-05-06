import shutil

#shutil.unpack_archive('Proyecto+Dia+9.zip', 'C:\\Users\\Zomber\\Desktop', 'zip' )
import re
import os
import time
import datetime
from pathlib import Path
import math

from Day_9.Dia9.medir_tiempo import duracion

inicio = time.time()

ruta = 'C:\\Users\\Zomber\\Desktop\\Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'

hoy = datetime.date.today()
num_encontrado = []
archivos_encontrado = []

def buscar_numero(archivo,patron):
    este_archivo = open(archivo,'r')
    texto = este_archivo.read()
    if re.search(patron,texto):
        return re.search(patron,texto)
    else:
        return ''
def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta,a),mi_patron)
            if resultado != '':
                num_encontrado.append(resultado.group())
                archivos_encontrado.append(a.title())
def mostrar_todo():
    indice = 0
    print('-'*50)
    print(f'Fecha de busqueda: {hoy}\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t-------')
    for a in archivos_encontrado:
        print(f'{a}\t\t{num_encontrado}')
        indice += 1
    print('\n')
    print(f'Numeros encontrados: {len(num_encontrado)}')
    fin = time.time()
    duracion = fin-inicio
    print(f'duracion de la busqueda: {math.ceil(duracion)}\n')
crear_listas()
mostrar_todo()

