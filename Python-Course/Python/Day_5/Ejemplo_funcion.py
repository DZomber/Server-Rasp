precios_cafe=[('capuchino',1),('Expreso',2.2),('Moka',1.9)]

def cafe_mas_caro(lista_precios):
    precio_mayor =0
    cafe_mas_caro = ''
    for cafe,precio in lista_precios:
        if precio>precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            print(f"el cafe {cafe} no es el mas caro")


    return (cafe_mas_caro,precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)

print(f"el cafe mas caro es {cafe} cuyo precio es {precio}")