import numpy as np

def f(x, y):
    return np.exp(-(x**2 + y**2))

def simpson_y(f, xval, N, spany):
    a, b = spany[0], spany[1] 
    dx = (b - a) / N
    I = 0.0
    curr = f(xval, a)
    mid = 0.0
    fwd = 0.0
    for i in range(0, N, 2):
        mid = f(xval, a + dx * (i + 1))
        fwd = f(xval, a + dx * (i + 2))

        val = (dx / 3) * (curr + 4*mid + fwd)
        
        I += val
        
        curr = fwd

    return I

def simpson(f, N, spanx):
    a, b = spanx[0], spanx[1]
    dx = (b - a) / N

    I = 0.0
    curr = simpson_y(f, a, N, [- np.sqrt(1 - a**2), np.sqrt(1 - a**2)])
    mid = 0.0
    fwd = 0.0
    
    for i in range(0, N, 2):
        mid = simpson_y(f, a + dx * (i + 1), N, [- np.sqrt(1 - (a + dx * (i+1))**2), np.sqrt(1 - (a + dx * (i+1))**2)] )
        fwd = simpson_y(f, a + dx * (i + 2), N, [- np.sqrt(1 - (a + dx * (i+2))**2), np.sqrt(1 - (a + dx * (i+2))**2)])

        I += (dx / 3) * (curr + 4*mid + fwd)
        
        curr = fwd

    return I

result = simpson(f, 500, [-1, 1])

print(f"The result of integral is: {result}")