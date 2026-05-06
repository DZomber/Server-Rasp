palabra = 'python'

lista = [letra for letra in palabra]
print(lista)

lista = [n for n in range(0,21,2)]
print(lista)

lista = [n for n in range(0,21,2) if n*2 > 10]
print(lista)

lista = [n if n*2 >10 else f'{n} no es > 10' for n in range(0,21,2)]
print(lista)

pies = [10,20,30,40,50]
metros = [p /3.281 for p in pies]
print(metros)