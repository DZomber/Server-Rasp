from sys import audit

mi_lista =[1,1,1,1,1,1,1]
print(len(mi_lista))

class Objeto:
    pass

mi_objeto=Objeto()
#print(len(mi_objeto)) #-> no tiene largo da error

class CD:
    def __init__(self,autor,titulo, canciones):
        self.autor=autor
        self.titulo=titulo
        self.canciones=canciones
    def __str__(self):
        return f'Album: {self.titulo} de {self.autor} con {self.canciones} canciones'
    def __len__(self):
        return self.canciones
    def __del__(self):
        print('Se ha eliminado el cd')

mi_cd = CD('Zoe', 'Rocanlover',13)
#del mi_cd # Elimina el cd jaja
print(mi_cd)
print(len(mi_cd))
