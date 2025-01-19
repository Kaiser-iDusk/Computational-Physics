import numpy as np

def f(z):
    func = np.tan(z) - (2 * z * np.sqrt(1 - (z ** 2)) / (2 * (z ** 2) - 1))
    return func 

def dfdx(z):
    dfx1 = (1 / np.cos(z)) ** 2
    dfx2 = (2 * (z ** 2) - 1) * (np.sqrt(1 - (z ** 2)) - ((z ** 3) / np.sqrt(1 - (z ** 2))))
    dfx3 = 4 * (z ** 2) * np.sqrt(1 - (z ** 2))
    dfx4 = (2 * (z ** 2) - 1) ** 2
    return dfx1 - 2 * ((dfx2 - dfx3) / dfx4)

epsilon = 1e-8
max_iter = 1000
found = True

iter = 0
z_init = 0.95

error = abs(f(z_init))

while(error > epsilon and iter <= max_iter):
    dfx = dfdx(z_init)

    if(dfx == 0):
        print("The derivative is zero, the root cannot be found!")
        found = False
        break
    z1 = z_init - f(z_init) / dfx
    z_init = z1

    error = abs(f(z_init))
    iter += 1

    print(f"Iteration: {iter} | z = {z_init} | f(z) = {f(z_init)} | error = {error}")

if found:
    if error > epsilon:
        print("Exact root not found. Terminated at 1000 iterations.")
    print(f"The root of the equation is z = {z_init}")
    f = 1 - (z_init ** 2)
    print(f"The non-trivial eigenvalue is E = -f = {-f}")

