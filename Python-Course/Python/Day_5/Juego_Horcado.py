from random import choice

palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra_elejida, letras_unicas = choice(lista_palabras), len(set(choice(lista_palabras)))
    return palabra_elejida, letras_unicas

def pedir_letra():
    letra_elejida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnopqrstuvwxyz'

    while not es_valida:
        letra_elejida = input('Elije una letra: ').lower()
        if letra_elejida in abecedario and len(letra_elejida) == 1:
            es_valida = True
        else:
            print('No has elegido una letra correcta')
    return letra_elejida

def mostrar_nuevo_tablero(palabra_elejida):
    lista_oculta = [l if l in letras_correctas else '-' for l in palabra_elejida]
    print(' '.join(lista_oculta))

def chequear_letra(letra_elejida, palabra_oculta, vidas, coincidencias):
    if letra_elejida in palabra_oculta:
        letras_correctas.append(letra_elejida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elejida)
        vidas -= 1

    if vidas == 0:
        return perder(), vidas, coincidencias
    elif coincidencias == letras_unicas:
        return ganar(palabra_oculta), vidas, coincidencias

    return False, vidas, coincidencias

def perder():
    print('Te has quedado sin vidas')
    print(f'La palabra oculta era {palabra}')
    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print(f'La palabra oculta era {palabra}')
    return True

palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\nLetras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()

    terminado, intentos, aciertos = chequear_letra(letra, palabra, intentos, aciertos)
    juego_terminado = terminado
