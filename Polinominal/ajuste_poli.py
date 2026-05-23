import numpy as np
import matplotlib.pyplot as plt

# 1. definir los datos de la tabla
x = np.array([0, 2, 3, 6, 7]) # fuerza (kgf)
y = np.array([0.12, 0.153, 0.17, 0.225, 0.260]) # longitud del resorte (m)

# vector x mas denso para que las graficas polinomiales se vean curvas y suaves
x_line = np.linspace(min(x), max(x), 100)

# 1 graficar los puntos en una grafica de dispersion
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='black', s=50, label='Datos Originales', zorder=5)

# 2) ajuste de polinomio de grado 2 y grafica
coef_2 = np.polyfit(x, y, 2)
y_2 = np.polyval(coef_2, x_line)
plt.plot(x_line, y_2, color='blue', label='Polinomio Grado 2')

# 3) ajuste de polinomio de grado 3 y grafica
coef_3 = np.polyfit(x, y, 3)
y_3 = np.polyval(coef_3, x_line)
plt.plot(x_line, y_3, color='orange', label='Polinomio Grado 3')

# 4) ajuste de polinomio de grado 4 y grafica
coef_4 = np.polyfit(x, y, 4)
y_4 = np.polyval(coef_4, x_line)
plt.plot(x_line, y_4, color='green', label='Polinomio Grado 4')

# configuraciones esteticas de la grafica
plt.title('Ajuste Polinomial: Alargamiento de un Resorte')
plt.xlabel('Fuerza (kgf)')
plt.ylabel('Longitud del resorte (m)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()