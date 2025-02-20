import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

q = 1  # Charge
m = 1  # Mass

def E_field(t, x, y, z):
    return np.array([0, 0.02, 0])  # Only in y direction

def B_field(t, x, y, z):
    return np.array([0, 0, 1 + 0.1*x + 0.01*t])  # Only in z direction

def G(t, state):
    x, y, z, vx, vy, vz = state
    E = E_field(t, x, y, z)
    B = B_field(t, x, y, z)
    v = np.array([vx, vy, vz])
    
    dvdt = (q/m) * (E + np.cross(v, B))
    return np.array([vx, vy, vz, dvdt[0], dvdt[1], dvdt[2]])

def rk4(time, f0, N):
    t0, t_final = time[0], time[1]
    dt = (t_final - t0) / N
    time_range = np.linspace(t0, t_final, N)
    trajectory = []
    velocity = []
    curr_f = f0

    for t in time_range:
        trajectory.append(curr_f[:3])
        velocity.append(curr_f[3:])
        
        # taking rk4 step
        k1 = dt * G(t, curr_f)
        k2 = dt * G(t + dt/2, curr_f + k1/2)
        k3 = dt * G(t + dt/2, curr_f + k2/2)
        k4 = dt * G(t + dt, curr_f + k3)
        curr_f = curr_f + (k1 + 2*k2 + 2*k3 + k4) / 6

    return np.array(trajectory), np.array(velocity)


def main():
    r0 = np.array([0, 0, 0])
    v0 = np.array([0, 0.1, 0])
    f0 = np.array([r0[0], r0[1], r0[2], v0[0], v0[1], v0[2]])
    time_range = [0, 100]
    N = 10000 # number of time steps

    trajectory, velocity = rk4(time_range, f0, N)

    # Plotting trajectory
    plt.figure(figsize=(8, 6))
    plt.plot(trajectory[:, 0], trajectory[:, 1], label='Particle Trajectory')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Trajectory of the Particle in the x-y Plane')
    plt.legend()
    plt.grid()
    plt.show()

    # 3D plot of velocity
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(velocity[:, 0], velocity[:, 1], velocity[:, 2], label='Velocity of the Particle')
    ax.set_xlabel('vx')
    ax.set_ylabel('vy')
    ax.set_zlabel('vz')
    ax.set_title('Velocity of the Particle')
    
    plt.show()


main()
