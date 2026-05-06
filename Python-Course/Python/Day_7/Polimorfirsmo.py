class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' Dice muuu')

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre+ ' Dice beee')

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

vaca1.hablar()
oveja1.hablar()
animales =[vaca1,oveja1]


for animal in animales:
    animal.hablar()

def animal_hablar(animal):
    animal.hablar()

animal_hablar(oveja1)
