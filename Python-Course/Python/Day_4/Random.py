#from random import randint

#aletorio = randint(1,50)
#print(aletorio)
from random import *
aletorio = round(uniform(1,5),1)
print(aletorio)

aletorio = random()
print(aletorio)

colores = ['Azul', 'Rojo', 'Verde','Amarillo']
aletorio = choice(colores)
print(aletorio)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)