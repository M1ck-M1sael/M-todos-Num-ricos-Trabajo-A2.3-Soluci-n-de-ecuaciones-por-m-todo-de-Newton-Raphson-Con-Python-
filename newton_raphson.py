# uso esta librería para las funciones matematicas
import math

# funcion original f(x)
def f(x):
    return x - math.exp(-5 * x)

# derivada f'(x)
def df(x):
    return 1 + 5 * math.exp(-5 * x)

def newton_raphson(x0, tolerancia):
    print(f"{"Iteracion":<12} | {"xi":<15} | {"Error absoluto":<15}")
    print("-" * 50)

    error = 1.0
    i = 0

    while error > tolerancia:
        # se aplica la formula de xi+1 = xi - f(xi) / f'(xi)
        xi_next = x0 - (f(x0) / df(x0))
        #caluclo de error absoluto
        error = abs(xi_next - x0)

        print(f"{i:<12} | {x0:<5.10f} | {error:<15.10e}")

        # actualizacion siguiente vux
        x0 = xi_next
        i += 1

    # ultima fila de la tolerancia
    print(f"{i:<12} | {x0:<15.10f} | {error:<15.103}")
    print("-" * 50)
    print(f"Raiz encontrada: {x0:.10f}")

# valores iniciales
valor_inicial = 0.5
limite_error = 1e-6

newton_raphson(valor_inicial, limite_error)