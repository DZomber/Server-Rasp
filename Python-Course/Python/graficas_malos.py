import matplotlib.pyplot as plt

def leer_resultados(archivo):
    with open('resultados_buenos.txt', 'r') as f:
        lineas = f.readlines()

    # Leer las últimas 5 líneas para obtener los valores
    min_val = float(lineas[-5].split(':')[-1].strip().replace('}', ''))
    max_val = float(lineas[-4].split(':')[-1].strip().replace('}', ''))
    promedio = float(lineas[-3].split()[-1])
    desviacion_std = float(lineas[-2].split()[-1])

    # Leer los datos crudos (primera parte del archivo)
    datos_neg_neu = [float(line.split(':')[-1].strip().replace('}', '')) for line in lineas if 'NEG-NEU' in line]

    return datos_neg_neu, min_val, max_val, promedio, desviacion_std


# Leer los datos desde el archivo
datos, min_val, max_val, promedio, desviacion_std = leer_resultados('resultadosMalos.txt')

# Generar las gráficas
# Gráfico de todos los datos de NEG/NEU
plt.figure(figsize=(10, 5))
plt.scatter(range(len(datos)), datos, color='blue', label='Datos NEG/NEU')

# Graficar el promedio y las bandas de desviación estándar
plt.axhline(promedio, color='red', linestyle='--', label='Promedio')
plt.fill_between(range(len(datos)), promedio - desviacion_std, promedio + desviacion_std,
                 color='orange', alpha=0.2, label='Desviación estándar')

# Etiquetas y título
plt.title('Gráfica de relación NEG/NEU')
plt.xlabel('Índice')
plt.ylabel('Valor NEG/NEU')
plt.legend()

# Mostrar la gráfica
plt.show()
