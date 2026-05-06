
def perfumeria():
    p = 0
    while True:
        p += 1
        yield p

def farmacia():
    f = 0
    while True:
        f += 1
        yield f

def cosmeticos():
    c = 0
    while True:
        c += 1
        yield c
a = perfumeria()
b = farmacia()
cx = cosmeticos()

def texto_turno(codigo,num):
    print('*'*23)
    print(f'Su turno es: {codigo} {num} ')
    print('aguarde y sera atendido')
    print('*'*23)
