monedas = 5
while monedas > 0:
    print(f'tengo {monedas} monedas')
    monedas -= 1
    if monedas == 0:
        print('Ya no tengo monedas')

respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n")
else: print('Gracias')
#pass = pasar
#break = interrumproi el loop actual
nombre = input("Tu nombre: ")
for letra in nombre:

    if letra == 'r':
        break
    print(letra)
#Continue
nombre = input("Tu nombre: ")
for letra in nombre:

    if letra == 'r':
        continue
    print(letra)