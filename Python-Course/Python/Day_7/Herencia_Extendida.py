class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')

class Pajaro(Animal):

    def __init__(self, edad, color,altura_vuelo):
        ''''
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo
        '''
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo
    def Hablar(self):
        print('pio')

    def Volar(self,metros):
        print(f'El pajaro vuela {metros} metros')
''''
piolin = Pajaro(3,'amarillo',60)

piolin.nacer()
piolin.Hablar()
piolin.Volar(5)

mi_animal = Animal(5,'cafe')
mi_animal.nacer()
'''

class Padre:
    def hablar(self):
        print('hola')
class Madre:
    def reir(self):
        print('ja ja')
    def hablar(self):
        print('Que tal')
class Hijo(Padre,Madre):
    pass
class Nieto(Hijo):
    pass
mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()
print(Nieto.__mro__)
mama = Madre()
mama.hablar()
mama.reir()

