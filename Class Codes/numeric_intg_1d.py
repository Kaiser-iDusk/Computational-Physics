import numpy as np

def f(x):
    return np.sin(x) / x

a = 0
b = 1
n = 1000

dx = (b-a) / n
I = 0.0

past = 1

for i in range(1, n+1):
    curr = f(a + i*dx)
    I += dx * 0.5 * (curr + past)
    # print(I)
    past = curr

print(f"After {n} iterations trapezoidal value is: {I}")