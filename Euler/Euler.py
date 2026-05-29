import numpy as np
import matplotlib.pyplot as plt

# defino la ecuacion diferencial y' = 2x - 3y
def df(x, y):
    return 2 * x - 3 * y

# funcion que ejecuta el metodo de Euler
def metodo_euler(x0, y0, xf, n):
    h = (xf - x0) / n
    x = np.array([x0])
    y = np.array([y0])
    
    for _ in range(n):
        y_next = y[-1] + h * df(x[-1], y[-1])
        x_next = x[-1] + h
        x = np.append(x, x_next)
        y = np.append(y, y_next)
        
    return x, y

# a) Euler con xf = 5 y n = 5
x_a, y_a = metodo_euler(0, 1, 5, 5)
print(f"a) yf para n=5: {y_a[-1]:.4f}")

# b) Euler con xf = 5 y n = 100
x_b, y_b = metodo_euler(0, 1, 5, 100)
print(f"b) yf para n=100: {y_b[-1]:.4f}")

# c) grafica para xf = 5, n = 100
plt.plot(x_b, y_b, color='blue', label='Método de Euler (n=100)')
plt.title("Solución numérica de y' = 2x - 3y")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()