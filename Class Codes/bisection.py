import numpy as np

def func(x):
    return np.tan(x) - np.exp(x)

a = 0.0
b = np.pi/2.0

eps = 1E-10

error = 1.0

while(error<eps):
    x0 = (a + b)/2.0
    if(func(x0) * func(a) < 0):
        b = x0
    else:
        a = x0
    print(f"x0 = {x0} | f(x0) = {func(x0)}")