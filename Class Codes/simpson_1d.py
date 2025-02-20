import numpy as np

def f(x):
    if x == 0:
        return 1
    
    return np.sin(x) / x

intv = [0, 1]
N = 1000

dx = (intv[1] - intv[0]) / N 
I = 0.0

for i in range(0, N, 2):
    I += (dx / 3) * (f(i * dx) + 4 * f((i+1) * dx) + f((i+2) * dx))

print(f"Simpson Integration = {I}")