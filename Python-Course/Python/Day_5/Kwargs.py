#Pasar valores completos

def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total


print(suma(x=3, y=5, z=2))
print('============')

def prueba(n1,n2,*args,**kwargs):
    print(f'el primer valor es {n1}')
    print(f'el segundo valor es {n2}')
    for arg in args:
        print(f"arg = {arg}")
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
prueba(1,2,3,4,y=5,z=2)

