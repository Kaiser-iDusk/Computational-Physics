import numpy as np

def f(x):
    return np.sin(x) / x

a = 0
b = 1
n = 10000000  

dx = (b-a) / n
I1 = 0.0
tol = 1e-12

for i in range(1, n+1):
    if(i < tol):
        curr = 1
    else:
        curr = f(a + i * dx)
    I1 += dx * curr

I2 = 0.0
past = 1

for i in range(1, n+1):
    curr = f(a + i*dx)
    I2 += dx * 0.5 * (curr + past)
    past = curr

print(f"Reimann : {I1}")
print(f"Trapezoidal: {I2}")

print(f"Error after {n} iterations: {I1 - I2}")
