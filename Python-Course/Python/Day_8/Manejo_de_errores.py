#Codigo
#try:
    #Codigo que queremos probar
#except:
    #Codigo a ejecutar si hay error
#else:
    #Codigo a ejecutar si no hay error
#finally:
    #Codigo que se va ejecutar de todos modos

def pedir_numero():

    while True:
        try:
            numero = int(input('Dame un Numero:'))

        except:
            print('Ese no es numero')
        else:
            print(f'Ingresaste el numero {numero}')
            break


    print('Gracias')
pedir_numero()