#Programa para calcular comisiones de empleados del %13 de ventas totales
nombre = input("Hola!, cual es tu nombre?")
print(f"Hola {nombre}")
ventas = input("Cuales han sido tus ventas totales?$")
ventas = int(ventas)
comision = ventas *13/100
comision = round(comision,2)

print(f"{nombre} tu comision de ${ventas} es ${comision} ")