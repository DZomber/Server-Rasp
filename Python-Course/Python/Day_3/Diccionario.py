diccionario = {'c1': 'valor1','c2':'valor2'}
print(diccionario)

cliente ={'Nombre':'Juan','Apellido':'Fuentes','Peso':55,'Talla':'M'}
consulta =(cliente['Nombre']+ " "+cliente['Apellido'])
print(consulta)

dic = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic['c2'][1].upper())

dic = {1:'a',2:'b'}
print(dic)
dic[3] = 'c'
print(dic)

dic[2] ='b'.upper()
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())