def devolver_distintos(n1,n2,n3):
    suma = n1+n2+n3
    lista = [n1,n2,n3]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return max(lista)
    else:
        lista.sort()
        return lista[1]

print(devolver_distintos(7,2,4))
