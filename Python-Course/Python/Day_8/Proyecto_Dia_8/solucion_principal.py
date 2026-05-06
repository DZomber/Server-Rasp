import solucion_numeros

def preguntar():

    print('Bienvenido a Farmacia Python')
    while True:
        print('[P] - Perfumeria\n[F] - farmacia\n[C] - cosmeticos')
        try:
            mi_rubro = input('ELija su rubro: ').upper()
            ["P","F","C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            break

    solucion_numeros.decorador(mi_rubro)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input('Quieres Sacar otro turno ? [S] [N]')
            ["S","N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion valida")

        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break
inicio()