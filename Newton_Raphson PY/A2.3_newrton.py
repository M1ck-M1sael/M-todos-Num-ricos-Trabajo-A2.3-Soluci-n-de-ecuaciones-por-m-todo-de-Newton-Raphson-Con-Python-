import numpy as np

def f(v):
    x, y = v
    # funciones del sistema
    f1 = x**2 + np.exp(y) - 5
    f2 = x*y**3 - 5*y - 8
    return np.array([f1, f2])

def jacobiano(v):
    x, y = v
    # derivadas parciales
    df1_dx = 2*x
    df1_dy = np.exp(y)
    df2_dx = y**3
    df2_dy = 3*x*y**2 - 5
    return np.array([[df1_dx, df1_dy], [df2_dx, df2_dy]])

def newton_raphson(v0, tol=1e-6, max_iter=100):
    v = v0
    print(f"{'Iter':<10} {'x':<15} {'y':<15} {'Error':<15}")
    print("-" * 55)
    
    for i in range(max_iter):
        F = f(v)
        J = jacobiano(v)
        
        # sistema J * delta = -F
        delta = np.linalg.solve(J, -F)
        v_next = v + delta
        
        error = np.linalg.norm(delta, np.inf)
        print(f"{i+1:<10} {v[0]:<15.8f} {v[1]:<15.8f} {error:<15.8e}")
        
        if error < tol:
            return v_next
        
        v = v_next
    
    return v

punto_inicial = np.array([-1.0, -1.0])
solucion = newton_raphson(punto_inicial)

print("-" * 55)
print(f"Solución final: x = {solucion[0]:.8f}, y = {solucion[1]:.8f}")