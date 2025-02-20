import numpy as np

# f" + sin(x) f' + f = 0

def p(x):
    return np.sin(x)

def q(x):
    return 1

def r(x):
    return 0

def finite_diff(N, range):
    dx = (range[1] - range[0]) / N
    D = np.zeros((N, N))
    S = np.zeros((N, 1))
    x = np.linspace(range[0], range[1], N)
    for i in range(0, N):
        D[i][i] = q(x[i]) - 2 / dx**2
        if i>0:
            D[i][i-1] = 1 / dx**2 - (p(x[i]) / (2 * dx))
        if i<N-1:
            D[i][i + 1] = 1 / dx**2 + (p(x[i]) / (2 * dx))
        S[i] = x[i]

    B = np.zeros((N, 1))
    B[0][0] = (1 / dx ** 2) -

def main():
    N = 100
    ans = finite_diff(N, [0, 4 * np.pi])
    print(ans)

main()