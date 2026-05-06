if 10 > 9:
    print('Es correcto')

if 5==2:
    print('son iguales!')
else: print('no son iguales')

mascota = 'perro'
if mascota == 'gato':
    print('tienes un gato')
elif mascota == 'perro':
    print('tienes un perro')
elif mascota == 'pez':
    print('tienes un pez')
else: print('no tienes un gato, ni un perro, ni un pez')

edad = 16
calificacion = 9
if edad < 18:
    print('eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else: print('No aprobado')
else: print('eres adulto')
