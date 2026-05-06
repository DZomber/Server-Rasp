lista = ['a','b','c']

for letras in lista:
    numero_letra = lista.index(letras)+1
    print(f'letra:{numero_letra} {letras}')

lista_nombre = ['Pablo','Laura','Fede', 'Luis','Julia']

for nombre in lista_nombre:
    print(f'hola {nombre}')

for nombre in lista_nombre:
    nombre.lower()
    if nombre.startswith('l'):
        print(f'hola {nombre}')
    else:
        print(f'hola {nombre} que no tiene "l" en su nombre')

numeros = {1,2,3,4,5,}
valor = 0

for numero in numeros:
    valor += numero
    print(valor)
print(valor)

palabra = 'Python es cool!'

for letra in palabra:
    print(letra)

for a, b in [[1,2],[2,3],[4,5]]:
    print(a)

dic = {'clave1': 'a', 'clave2': 'b','clave3': 'c'}

for items in dic:
    print(items)

for items in dic.items():
    print(items)
for items in dic.values():
    print(items)