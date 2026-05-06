mi_archivo = open ('prueba.txt')
def prueba_leer_todo_archivo():
    print(mi_archivo.read()) #lee todo el archivo

def prueba_una_linea():
    una_linea = mi_archivo.readline()
    print(una_linea.upper())#lee solo una linea

    una_linea = mi_archivo.readline()
    print(una_linea.lower())#lee solo una linea

    una_linea = mi_archivo.readline()
    print(una_linea)#lee solo una linea

def prueba_aqui_dice():
    for l in mi_archivo:
        print(f'Aqui dice: {l}')

def prueba_todas():
    todas = mi_archivo.readlines()
    print(todas)
#prueba_leer_todo_archivo()
#prueba_una_linea()
#prueba_aqui_dice()
prueba_todas()


mi_archivo.close()