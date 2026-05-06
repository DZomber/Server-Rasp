x1 = [0,0,1,1]
x2 = [0,1,0,1]
t =  [0,0,0,1]
et = []
yt = []
# Pesos iniciales
w1 = 0.8
w2 = -0.5
beta = 0.5  # Tasa de aprendizaje ajustada
bias = 0
bias_total =[]

while True:
    contador_errores = 0
    for i in range(len(t)):
        print(f'\nIteración {i + 1}:')
        print(f'x1 = {x1[i]}\nx2 = {x2[i]}\n t = {t[i]}')

        # Cálculo de la suma ponderada
        u = (w1 * x1[i] + w2 * x2[i]) - bias
        print(f'u = ({w1:.2f}) * ({x1[i]:.2f}) + ({w2:.2f}) * ({x2[i]:.2f})- {bias} = {u:.2f}')

        # Función de activación (umbral en 0)
        y = 1 if u >= 0 else 0
        yt.append(y)
        print(f'y = {y}')

        # Verificación de error
        E = t[i] - y
        print(f'E = {t[i]} - {y} = {E}')
        et.append(E)
        contador_errores += abs(E)

        # Actualización de pesos si hay error
        if E != 0:
            delta_w1 = beta * x1[i] * E
            delta_w2 = beta * x2[i] * E
            w1 += delta_w1
            w2 += delta_w2
            bias -= beta * E
            print(f'Nuevo bias -> bias: {bias:.2f}')
            bias_total.append(bias)

            print(f'Nuevos pesos -> w1: {w1:.2f}, w2: {w2:.2f}')

            # **Recalcular u y y después de actualizar pesos**
            u = (w1 * x1[i] + w2 * x2[i]) - bias
            y = 1 if u >= 0 else 0

            yt[-1] = y  # Actualizar el valor en la lista de resultados
            print(f'Nueva evaluación: u = {u:.2f}, y = {y}')
    if contador_errores == 0:
        break
print(f'\nResultados finales:')
print(f'Y = {yt}')
print(f'E = {et}')
print(f't = {t}')
print(f'bias = {bias_total}')
print(f'w1 = {w1:.2f}, w2 = {w2:.2f}')


