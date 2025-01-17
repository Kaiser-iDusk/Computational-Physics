import numpy as np

def f(x):
    return np.sin(x) / x

a = 0
b = 1
n = 1000

dx = (b-a) / n
I = 0.0
tol = 1e-12

for i in range(1, n+1):
    if(i < tol):
        curr = 1
    else:
        curr = f(a + i * dx)
    I += dx * curr
    # print(I)
    # past = curr

print(f"After {n} iterations reimann value is: {I}")