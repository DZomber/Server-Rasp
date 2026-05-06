import os
from  pathlib import Path
import sys
ruta = Path('C:\\Users\\Zomber\\Documents\\Curso Udemy\\PYTHON\\Recetas')
categorias = ['Carnes', 'Ensaladas', 'Pastas', 'Postres']



def mostrar_ruta():
    print(ruta)
    return print(f'La carpeta de las recetas se encuentra en = "{ruta}"')
def cantidad_recetas():
    total_recetas = 0
    for categoria in categorias:
        carpeta = ruta / categoria
        total_recetas = total_recetas + len(list(carpeta.iterdir()))

    return print(f'hay un total de {total_recetas} recetas')
def categorias_totales():
    contador_categorias = 0
    for i in os.listdir(ruta):
        contador_categorias += 1
        print(f'{contador_categorias}){i}')
    escojer = int(input('->'))
    escojer -= 1
    contador_archivos = 0

    while escojer not in range(contador_categorias):
        print(f'EL valor {escojer + 1} no esta en rango')
        escojer = int(input('->'))
        escojer -= 1
    return contador_categorias, escojer, contador_archivos
def opcion_1():
    print('Que categoria quieres abrir?')
    contador_categorias, escojer, contador_archivos = categorias_totales()
    if escojer in range(contador_categorias):
        print(f'Que archivos de la carpeta {os.listdir(ruta)[escojer]} quieres abrir?')
        x = f'C:\\Users\\Zomber\\Documents\\Curso Udemy\\PYTHON\\Recetas\\{os.listdir(ruta)[escojer]}'
        for i in os.listdir(x):
            contador_archivos += 1
            print(f'{contador_archivos}){i}')
        receta = int(input('->'))
        receta -=1
        while receta not in range(contador_archivos):
            print(f'EL valor {receta+1} no esta en rango')
            receta = int(input('->'))
            receta -= 1
        if receta in range(contador_archivos):
            print(open(f'C:\\Users\\Zomber\\Documents\\Curso Udemy\\PYTHON\\Recetas\\{os.listdir(ruta)[escojer]}\\{str(os.listdir(x)[receta])}').read())
        else:
            print('no esta disponible')
            print(receta)

def opcion_2():
    contador_categorias, escojer, contador_archivos = categorias_totales()
    print(f'Que nombre le quieres poner a tu receta?')
    nombre_receta = input('->')
    # Asegúrate de que la carpeta existe
    os.makedirs(f'C:\\Users\\Zomber\\Documents\\Curso Udemy\\PYTHON\\Recetas\\{os.listdir(ruta)[escojer]}', exist_ok=True)
    # Crear y abrir el archivo para escribir
    with open(f'C:\\Users\\Zomber\\Documents\\Curso Udemy\\PYTHON\\Recetas\\{os.listdir(ruta)[escojer]}\\{nombre_receta}.txt', 'w') as abierto:
        texto_receta = input('Introduce la receta aquí: ')
        abierto.write(texto_receta)
def opcion_3():
    print(f'Que nombre le quieres poner a tu categoria?')
    nombre_carpeta= input('->')
    # Asegúrate de que la carpeta existe
    os.makedirs(f'C:\\Users\\Zomber\\Documents\\Curso Udemy\\PYTHON\\Recetas\\{nombre_carpeta}', exist_ok=True)
def opcion_4():
    contador_categorias, escojer, contador_archivos = categorias_totales()
    if escojer in range(contador_categorias):
        print(f'Que archivos de la carpeta {os.listdir(ruta)[escojer]} quieres eliminar?')
        x = f'C:\\Users\\Zomber\\Documents\\Curso Udemy\\PYTHON\\Recetas\\{os.listdir(ruta)[escojer]}'
        for i in os.listdir(x):
            contador_archivos += 1
            print(f'{contador_archivos}){i}')
        receta = int(input('->'))
        receta -= 1
        while receta not in range(contador_archivos):
            print(f'EL valor {receta + 1} no esta en rango')
            receta = int(input('->'))
            receta -= 1
        if receta in range(contador_archivos):
            os.remove(f'C:\\Users\\Zomber\\Documents\\Curso Udemy\\PYTHON\\Recetas\\{os.listdir(ruta)[escojer]}\\{str(os.listdir(x)[receta])}')


def opcion_5():
    print(f'Que categoria quieres eliminar?')
    contador_categorias, escojer, contador_archivos = categorias_totales()
    if escojer in range(contador_categorias):
        categoria_eliminar = os.listdir(ruta)[escojer]
        print(f'Eliminando la carpeta {categoria_eliminar}')
        os.rmdir(ruta / categoria_eliminar)
def opcion_6():

    # Código antes de terminar
    print("Este es el final del script.")

    # Salida del script
    sys.exit()


def comenzar():
    print('Bienvenido a los recetarios')
    mostrar_ruta()
    cantidad_recetas()

    print()
    for i in range(1, 7):
        print(f'Opcion {i})')
    opcion = int(input('Elija una opcion: \n' + '->'))
    while opcion not in range(1, 7):
        print('Opcion invalida')
        opcion = int(input('->'))

    if opcion == 1:
        opcion_1()
    elif opcion == 2:
        opcion_2()
    elif opcion == 3:
        opcion_3()
    elif opcion == 4:
        opcion_4()
    elif opcion == 5:
        opcion_5()
    elif opcion_6():
        opcion_6()
comenzar()


def presionar_tecla():
    tecla = input('Presiona una tecla para continuar: ')
    while tecla == tecla:
        comenzar()
presionar_tecla()




