texto = "Este es el texto de Zomber"
resultado = texto.upper()
print(resultado)
resultado = texto[2].upper()
print(resultado)
resultado = texto.lower()
print(resultado)

resultado = texto.split()
print('split',resultado)

resultado = texto.split("t")
print(resultado)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e =" ".join([a, b, c, d])
print(e)

resultado = texto.find("Z")
print(resultado)

resultado = texto.replace("Zomber", "Python")
print(resultado)


