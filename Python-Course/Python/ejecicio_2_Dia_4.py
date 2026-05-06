def orden_afa_palabra(palabra):
    mi_set =set()
    for letra in palabra:
        mi_set.add(letra)
    mi_lista = list(mi_set)
    mi_lista.sort()
    return mi_lista

print(orden_afa_palabra("diegooo"))


import random

moneda = ['Cara', 'Cruz']
lista_numeros = [1, 2, 15, 7, 2, 8]

# Función para lanzar la moneda
def lanzar_moneda():
    resultado = random.choice(moneda)
    return resultado

def probar_suerte(resultado,lista):
    if resultado == 'Cara':
        print("La lista se autodestruira")
        return []
    elif resultado == 'Cruz':
        print(f"La lista fue salvada {lista_numeros}")
        return lista

print(lanzar_moneda())
nueva_lista = probar_suerte(resultado=lanzar_moneda(), lista=lista_numeros)