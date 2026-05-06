def mi_funcion():
    #return 4
    lista = []
    for x in range(1,5):
        lista.append(x*10)
    return lista
# return pruduce el numero 4 y lo ha devuelto
def mi_generador():
    #yield 4
    for x in range(1,5):
        yield x*10

print(mi_funcion())
print(mi_generador())
g = mi_generador()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print('*'*10)
def mi_generado2():
    x = 1
    yield x
    x +=1
    yield x
    x +=1
    yield x
g2 = mi_generado2()
print(next(g2))
print(next(g2))
print(next(g2))