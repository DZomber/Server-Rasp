from random import shuffle # -> libreria interna de Python para shuffle
#lista inicial
palitos = ['-', '--','---','----']

#Mezclar palitos
def  mezclar(lista):
    shuffle(lista)
    return lista

#print(mezclar(palitos)) # -> combrobar funcion de arriba
#Pedir intento
def probar_suerte():
    intento =''
    while intento not in ['1','2','3','4']:
        print(f'el valor {intento} no esta en el rango')
        intento = input('Elije un numero del 1 aL 4 ')

    return int(intento)


#Comprobar intentos
#intento1 = probar_suerte()
#print(intento1)
def chequear_intento(lista,intento):
    if lista[intento-1] == '-':
        print('a lavar los platos!')
    else: print('Te has salvado')
    print(f'Te ha tocado {lista[intento-1]}')

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)