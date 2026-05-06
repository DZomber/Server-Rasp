import sys
class  Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre, apellido,numero_cuenta,balance =0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f' EL  Sr {self.nombre} {self.apellido} Num.Cuenta  ={self.numero_cuenta} con un balance de  ${self.balance}'

    def depositar(self, deposito):
        self.balance += deposito
        return f'Se ha depositado {deposito}\n Total= {self.balance} '

    def retirar(self, retiro):
        if self.balance > retiro:
            self.balance -= retiro
            return f'Se ha retirado  {retiro} '
        else: return 'No tiene el monto suficiente para retirar'

def crear_cliente():
    a = input('Cual es tu nombre?')
    b = input('Cual es tu apellido?')
    c = int(input('Cual es tu numero de cuenta?'))
    client = Cliente(a,b,c)
    return client
my_cliente = crear_cliente()

#Inicio
def inicio():
    x = 0

    menu = ['Informacion del cliente', 'Depositar', 'Retirar','Salir']
    while x !='4':
        for i, item in enumerate(menu,1):

            print(f'{i}){item}')
        x = int(input('Escoje una opcion?'))
        if x == 1:
            print(my_cliente)
            print('Se ha registrado el cliente')
        if x == 2:
            depositar = int(input('Cuanto vas a depositar?'))

            print(my_cliente.depositar(depositar))
        if x == 3:
            retirar = int(input('Cuanto va retirar?'))
            print(my_cliente.retirar(retirar))
        if x == 4:
            print("Hasta la Proxima.")

            # Salida del script
            sys.exit()

inicio()



