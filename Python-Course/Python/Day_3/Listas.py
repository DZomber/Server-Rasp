mi_lista = ['a','b','c']
otra_lista =["Hola", 55,6.1]
resultado = len(mi_lista)
print(resultado)
resultado = mi_lista[0:]
print(resultado)
resultado = mi_lista + otra_lista
print(resultado)
mi_lista3 = mi_lista + otra_lista
mi_lista3.append("g")
mi_lista3.pop(3)
print(mi_lista3)
