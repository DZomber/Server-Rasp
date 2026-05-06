import zipfile
import send2trash
import shutil
def eliminar_archivo():
    send2trash.send2trash('archivo_a.txt')
    send2trash.send2trash('archivo_b.txt')
    send2trash.send2trash('archivo_comprimido.zip')

def crear_archivo():
    a = open('archivo_a.txt','w')
    a.write('soy el texto a')
    b = open('archivo_b.txt', 'w')
    b.write('soy el texto b')
    return a, b
def funcion_comprimir():
    mi_zip = zipfile.ZipFile('archivo comprimido.zip', 'w')
    mi_zip.write('archivo_a.txt')
    mi_zip.write('archivo_b.txt')
def usando_zipfile():
    zip_abierto = zipfile.ZipFile('archivo comprimido.zip', 'r')
    zip_abierto.extractall('archivo_comprimido.zip')
def usando_shufil():
    carpeta ='C:\\Users\\Zomber\\Documents\\Curso Udemy\\PYTHON\\Python\\Day_9'
    archivo_destino = 'Todo_comprimido'
    shutil.make_archive(archivo_destino, 'zip', carpeta)
    shutil.unpack_archive('Todo_comprimido.zip','Dia9')

#crear_archivo()
#eliminar_archivo()
#funcion_comprimir()
usando_shufil()
