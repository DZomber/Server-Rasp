from pathlib import Path

base = Path.home()
guia = Path(base,'Barcelona','Sagrada_Familia')
guia2 = Path(base,'Europa','España',Path('Bercelona','Sagrada_Familia'))
guia3 = guia2.with_name('La_Pedrera.txt')

print(base)
print(guia)
print(guia2)
print(guia3)
print(guia.parent)
print('*'*20)
guia4 = Path(Path.home(),'Europa')
print(guia4)
for txt in Path(guia4).glob('**/*.txt'):
    print(txt)