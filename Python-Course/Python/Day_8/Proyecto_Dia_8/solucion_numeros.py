def numeros_perfumeria():
    for n in range(1,1000):
        yield f"P- {n}"


def numeros_farmacia():
    for n in range(1, 1000):
        yield f"P- {n}"


def numeros_cosmeticos():
    for n in range(1, 1000):
        yield f"P- {n}"
p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmeticos()

def decorador (rubro):
    print("\n"+ "*"*23)
    print("Su numero es:")
    if rubro =='P':
        print(next(p))
    elif rubro =='F':
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y sera Atendido")
    print("*"*23)