

x1 = [0.3, -0.6, -0.1, 0.1]
x2 = [0.7, 0.3, -0.8, -0.45]
t = [1, 0, 0, 1]
et = []
yt = []

# Pesos iniciales
w1 = 0.8
w2 = -0.5
beta = 0.5  # Tasa de aprendizaje ajustada

while True:
    contador_errores = 0
    for i in range(len(t)):
        print(f'\nIteración {i + 1}:')
        print(f' x1 = {x1[i]}\n x2 = {x2[i]}\n t = {t[i]}')

        # Cálculo de la suma ponderada
        u = w1 * x1[i] + w2 * x2[i]
        print(f'u = ({w1:.2f}) * ({x1[i]:.2f}) + ({w2:.2f}) * ({x2[i]:.2f}) = {u:.2f}')

        # Función de activación (umbral en 0)
        y = 1 if u >= 0 else 0
        yt.append(y)
        print(f'y = {y}')

        # Verificación de error
        E = t[i] - y
        print(f'E = {t[i]} - {y} = {E}')
        et.append(E)

        # Actualización de pesos si hay error
        if E != 0:
            delta_w1 = beta * x1[i] * E
            delta_w2 = beta * x2[i] * E
            w1 += delta_w1
            w2 += delta_w2
            print(f' Nuevos pesos -> w1: {w1:.2f}, w2: {w2:.2f}')
            contador_errores += abs(E)

            # **Recalcular u y y después de actualizar pesos**
            u = w1 * x1[i] + w2 * x2[i]
            y = 1 if u >= 0 else 0
            yt[-1] = y  # Actualizar el valor en la lista de resultados
            print(f' Nueva evaluación: u = {u:.2f}, y = {y}')
    if contador_errores == 0:
        break

print(f'\nResultados finales:')
print(f'Y = {yt}')
print(f'E = {et}')
print(f't = {t}')

