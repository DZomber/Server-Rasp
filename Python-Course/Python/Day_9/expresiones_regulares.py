import re # re -> expresiones regulares

texto = 'Si necesitas ayuda llama al (658)- 598-9977 las 24 horas al servicio de ayuda online'

patron = 'nada'
patron1 = 'ayuda'

busqueda = re.search(patron, texto)
print(busqueda)
busqueda = re.search(patron1, texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())


busqueda = re.findall(patron1, texto)
print(busqueda)
print(len(busqueda))



for hallazgo in re.finditer(patron1, texto):
    print(hallazgo.span())
print('*'*25)

texto1 = 'llama al 564-525-6588 ya mismo'
patron2 = r'\d\d\d-\d\d\d-\d\d\d\d' #los caracteres que encuentre aqui debe tratarlos como caracteres de un patron de una expresion regular

resultado = re.search(patron2, texto1)
print(resultado)
print(resultado.group())

patron3 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado2 = re.search(patron3, texto1)
print(resultado2.group(1))
print(resultado2.group(2))
print(resultado2.group(3))
print('****'*25)
#Usuario va generar una clave y comprobar si cumple algunas condiciones
#Comprobar si inicia con una letra
# w < - significa alfa numerico

'''
clave = input('Clave: ')
patron4 = r'\D{1}\w{7}'
chequear = re.search(patron4, clave)
print(chequear)
'''
print('****'*25)

#Operadores especiales
mensaje = 'No atendemos los lunes por la tarde'
buscar = re.search(f'lunes|martes',mensaje)
print(buscar)
buscar = re.search(f'....demos....',mensaje) # acomodin
print(buscar)
buscar = re.search(r'^\D',mensaje)#Buscar si hay patron al inicio de un string
print(buscar)
buscar = re.search(r'\D$',mensaje)#Buscar si hay patron al inicio de un string
print(buscar)
buscar = re.findall(r'[^s]+',mensaje)#Buscar si hay patron al inicio de un string
print(buscar)