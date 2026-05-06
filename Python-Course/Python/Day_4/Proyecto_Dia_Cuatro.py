#Este proyecto consiste en el juego de adivinar el numero
from random import *

nombre = input('Hola, como te llamas?\n ->')
print(f'Hola {nombre} es un gusto, vamos a jugar adivina el numero\n Te parece? S/N')
respuesta_Jugar = input().upper()
#Inicia un bucle while si se introduce otro caracter no deseado se repetira hasta contestar bien
while respuesta_Jugar != 'N' and respuesta_Jugar != 'S':
    print("No es respuesta valida, solo respondo con 'S' o 'N'")
    respuesta_Jugar = input().upper()
#si la respuesta es n, se terminara el codigo
if respuesta_Jugar == 'N':
    print(f'Esta bien, nos vemos {nombre}')
    exit()
else: print('Vale, tienes 8 intentos Ok? el numero esta entre el 1 al 100')
intentos = 8
intentos_tomados = 0
numero_adivinado = randint(1,100)

while intentos > 0:
    print(f'Tienes {intentos} intentos')
    numero = int(input('Introduce un numero: '))
    print(f'El numero introducido es {numero}')
    if numero < 1 or numero > 100:
        print('El numero introducido no esta permitido')
        intentos -= 1
        intentos_tomados += 1
    elif numero < numero_adivinado:
        print('Mi numero es mas alto')
        intentos -= 1
        intentos_tomados += 1
    elif numero > numero_adivinado:
        print('Mi numero es menos alto')
        intentos -= 1
        intentos_tomados += 1
    elif numero == numero_adivinado:
        print(f"Felicidades adivinaste el numero, te tomaron {intentos_tomados} ")
        break
else: print(f'Lo siento, perdiste :(\nEl numero a adivinar era {numero_adivinado}')





