import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def acc(r, t):
    return np.array([[np.sin(r[1][0])], [np.cos(r[0][0])]])

def verlet(r0, v0, time, dt):
    t = np.linspace(time[0], time[1], int((time[1] - time[0])/dt))
    x_m = r0 - dt * v0 + 0.5 * dt**2 * acc(r0, 0)
    x = r0
    gen_results = []
    k = 0
    for i in t:
        x_p = -x_m + 2 * x + dt**2 * acc(x, i)
        gen_results.append(x)
        x_m = x
        x = x_p

    return np.array(gen_results)

r0 = np.array([[0], [0]])
v0 = np.array([[0], [0]])
time = [0, 50]

dt = 1e-2

results = verlet(r0, v0, time, dt)
results = results.reshape(-1, 2)
print(results.shape)

plt.figure()
plt.title('Trajectory')
plt.plot(results.T[0], results.T[1])
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.figure()
plt.plot(np.linspace(time[0], time[1], int((time[1] - time[0])/dt)), results.T[0])
plt.title('x_pos vs time')
plt.xlabel('time')
plt.ylabel('x_pos')
plt.show()

plt.figure()
plt.plot(np.linspace(time[0], time[1], int((time[1] - time[0])/dt)), results.T[1])
plt.title('y_pos vs time')
plt.xlabel('time')
plt.ylabel('y_pos')
plt.show()

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data
z = results.T[1]
y = results.T[0]
x = np.linspace(time[0], time[1], int((time[1] - time[0])/dt))
c = x + y

# Plot 3D scatter
ax.scatter(x, y, z, c=c)
ax.set_title('3D Scatter Plot')
ax.set_xlabel('Time')
ax.set_ylabel('x_pos')
ax.set_zlabel('y_pos')

# Show plot
plt.show()