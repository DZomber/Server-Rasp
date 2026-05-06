from numeros import *
import sys

def selec_area():

    while True:

        try:

            print("Que area desea elegir: ")
            categorias = ['Perfumeria', 'Farmacia', 'Cosmeticos']
            for i, item in enumerate(categorias,1):
                print(f'{i}. {item}')
            fx = int(input('->'))
            if fx == 1:
                texto_turno('P-',next(a))

            elif fx == 2:
                texto_turno('F-',next(b))

            elif fx == 3:
                texto_turno('C-',next(cx))

            else:
                print(f'el numero {fx} esta fuera del rango disponible')
                selec_area()
        except ValueError:
            print("Se esperaba un numero")
            selec_area()
        finally:
            turno()

def turno():
    num_turno = input('Desea sacar otro turno?\n"s" "n"\n')
    if num_turno == 's':

        selec_area()
    elif num_turno == 'n':
        print('Gracias por usar el sistema elaborado por <Zomber.exe>')
        sys.exit()
    else:
        print('Solo se espera un "s" o "n" como respuesta')
        turno()

print('Bienvenido a la Farmacia')
selec_area()