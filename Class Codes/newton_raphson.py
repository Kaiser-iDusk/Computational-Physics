import numpy as np

def dfdx(x):
    return (1/np.cos(x))**2 - np.exp(x)

def f(x):
    return np.tan(x) - np.exp(x)

x0 = 1.57
iter = 0
max_iter = 20
eps = 1e-10
error = np.abs(f(x0))

while(error > eps and iter <= max_iter):
    # if (dfdx(x0) < eps):
    #     break
    x1 = x0 - (f(x0) / dfdx(x0))
    error = abs(f(x1))
    x0 = x1
    iter += 1

    print(f"Iteration = {iter} | x0 = {x0} | f(x0) = {f(x0)} | error = {error}")