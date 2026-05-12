def f(x):
    return x - 0.6 * x**3

def derivativa_numerica(x, h):
    return (f(x + h) - f(x)) / h

x_val = 0.5
h_values = [0.25, 0.1, 0.01]
valor_real = 0.55

print(f"{'h':<10} | {'Aproximación':<15} | {'Error Absoluto':<15}")
print("-" * 45)

for h in h_values:
    aprox = derivativa_numerica(x_val, h)
    error = abs(valor_real - aprox)
    print(f"{h:<10} | {aprox:<15.6f} | {error:<15.6f}")