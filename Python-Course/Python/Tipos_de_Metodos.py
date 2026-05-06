class Pajaro:
    alas = True
    def __init__(self, color,especie):
        self.color = color
        self.especie = especie
    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'el pajaro ha volado {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color ='negro'

    @classmethod
    def pomer_huevos(cls, cantidad):
        print(f'puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print('El pajaro mira')
piolin = Pajaro('amarillo', 'canario')
piolin.pintar_negro()
piolin.alas = False
print(piolin.alas)
Pajaro.pomer_huevos(5)
Pajaro.mirar()
