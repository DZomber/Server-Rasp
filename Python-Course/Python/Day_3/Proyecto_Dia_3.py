texto = input("Ingrese un texto: ").lower()
#pedir al usuario 3 letras al azar
letra1 = input("Ingrese una letra: ").lower()
letra2 = input("Ingrese una letra: ").lower()
letra3 = input("Ingrese una letra: ").lower()
#Convertir las letras en una lista
letras = list((letra1 + letra2 + letra3))
print("El texto introducido es: ", texto)
print(f'Las letras han sido {letras}')
#texto = texto.lower()
#Conteo de letras repetidas en el texto
letra_repetida1 = texto.count(letras[0])
letra_repetida2 = texto.count(letras[1])
letra_repetida3 = texto.count(letras[2])
print(f'la letra {letra1} aparece {letra_repetida1} vece(s)')
print(f'la letra {letra2} aparece {letra_repetida2} vece(s)')
print(f'la letra {letra3} aparece {letra_repetida3} vece(s)')
#dividir el texto por palabras con .split
total_palabras = texto.split()
#conteo de pabras con len()
print(f'El texto tiene {len(total_palabras)} palabras')
#Se usa un index en la posicion [0] que es la primera letra y [-1] que es la ultima
primer_letra = texto[0]
print(f'la primera letra del texto es: {primer_letra}')
ultima_letra = texto[-1]
print(f'la ultima letra es: {ultima_letra}')
#Texto con al revez con [::-1]
#print(f'la texto al revez es: {total_palabras[::-1]}')
print(f'la texto al revez es: {'-'.join(total_palabras[::-1])}')

palabra_texto = 'python' in texto
print(palabra_texto)
dic = {True:"si", False:"no"}
print(f"La palabra 'Python' {dic[palabra_texto]} esta")