from random import choice

def palabra_azar():
    palabras = ['Manzana', 'Television', 'Perico', 'Sarten', 'Videos']
    palabra = choice(palabras)
    return palabra

palabra_hecha = palabra_azar()

def comenzar_juego(palabra):
    guiones_diccionario = {
        'Manzana': '1-------',
        'Television': '2----------',
        'Perico': '3------',
        'Sarten': '4------',
        'Videos': '5------'
    }
    guiones = guiones_diccionario.get(palabra, '------')
    print(guiones)
    return guiones

print('Vamos a jugar el juego del ahorcado, tienes un total de 6 vidas. La palabra es la siguiente:')
guiones = comenzar_juego(palabra_hecha)

vidas = 6

def prueba(palabra):
    global vidas
    resultado = '-' * len(palabra)
    letras_adivinadas = set()
    while vidas > 0:
        intento = input('Ingrese una letra: ').lower()
        if intento in letras_adivinadas:
            print('Ya intentaste esa letra. Prueba con otra.')
            continue
        letras_adivinadas.add(intento)

        if intento in palabra.lower():
            nuevo_resultado = ''
            for i in range(len(palabra)):
                if palabra[i].lower() == intento:
                    nuevo_resultado += palabra[i]
                else:
                    nuevo_resultado += resultado[i]
            resultado = nuevo_resultado
            print(f'¡Bien hecho! La palabra es: {resultado}')
        else:
            vidas -= 1
            print(f'No hay {intento} en la palabra. Te quedan {vidas} vidas.')

        if '-' not in resultado:
            print(f'¡Felicidades! Adivinaste la palabra {palabra}')
            break
    else:
        print(f'Lo siento, perdiste. La palabra era: {palabra}')

prueba(palabra_hecha)
