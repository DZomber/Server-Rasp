def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minusculas(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minusculas
operacion = cambiar_letras('may')
operacion('Palabra')
operacion = cambiar_letras('min')
operacion('Palabra')

def decorar_saludo(funcion):

    def otra_funcion(texto):
        print('hola')
        funcion(texto)
        print('adios')
    return otra_funcion
#@decorar_saludo
def mayus(texto):
    print(texto.upper())

def minus(texto):
    print(texto.lower())

mayuscula_decorada = decorar_saludo(mayus)
minusculas_decorada = decorar_saludo(minus)
mayus('Python')
minus('Python')
