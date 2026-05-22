def f(x):
    # defino la funcion de la integral
    return 1 - 0.3*x + 0.08*(x**2) - 0.0012*(x**5)

# parametros iniciales
a = 2
b = 4
n = 4

# calculo del incremento (h)
h = (b - a) / n

# inicio la sumas de los terminos
suma_impar = 0
suma_par = 0

# suma de terminos impares
for i in range(1, n, 2):
    suma_impar += f(a + i * h)

# suma de terminos pares
for j in range(2, n, 2):
    suma_par += f(a + j * h)

# aplico la formula de Simpson 1/3 de aplicacion multiple
integral = (h / 3) * (f(a) + 4 * suma_impar + 2 * suma_par + f(b))

# en el video lo hace dirente: en el video usan (b - a) * (...) / (3 * n)
# pero h/3 es algebraicamente idéntico y mas limpio.

print(f"Resultado aproximado de la integral con n={n} es: {integral}")