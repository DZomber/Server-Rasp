#Conversiones Implicitas


num1 = 20
num2 = 30.5

num1 += num2

print(type(num1))
print(type(num2))
#Conversiones Explicitas
num1 = 5.8
print(num1)
print(type(num1))
num2 = int(num1)
print(num2)
print(type(num2))

edad = input("Dime tu edad: ")
print(type(edad))
edad = int(edad)
print(type(edad))
nueva_edad = edad + 1
print("Tu nueva edad es ", nueva_edad)

