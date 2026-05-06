"""""
def chequear_3_cifras(numero):
    return numero in range(100,1000)
#resultado = chequear_3_cifras(65)
suma = 586 + 402
resultado = chequear_3_cifras(suma)
print(suma)
print(resultado)
"""
def chequear_3_cifras(lista):
    lista_3_cifras = []
   # return n in range(100,1000)
    for i in lista:
        if i in range(100,1000):
            lista_3_cifras.append(i)
        else:
            pass
    #return False # -> el return False es hasta el final del bucle para verificar si los 3 nummeros estan en el rango o no
    return lista_3_cifras

resultado = chequear_3_cifras([55,99,600])
#resultado = chequear_3_cifras([555,99,6000])
#resultado = chequear_3_cifras([555,99,600])



