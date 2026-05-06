import os
import shutil
import send2trash
#send2trash.send2trash('C:\\Users\\Zomber\\Desktop\\curso.txt')
print(os.getcwd())

archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()
print(os.listdir())

shutil.move('curso.txt', 'C:\\Users\\Zomber\\Desktop')