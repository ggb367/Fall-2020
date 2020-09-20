import numpy as np
import matplotlib.pyplot as plt

r = 8717.36
r_i_0 = np.array([r, 0, 0])
mu = 398600.4418
v_i_0 = np.array([0, (mu/r)**.5, 0])
s_b = np.array([1/2**.5, 0, 1/2**.5])
w = 2*np.pi/(135*60)


def t_inertial_to_body(t):
    return np.array([[np.sin(w*t), np.cos(w*t), 0], [0, 0, -1], [-np.cos(w*t), np.sin(w*t), 0]])


time_series = np.arange(0, 135*60)
s_x = []
s_y = []
s_z = []
for step in time_series:
    temp = np.matmul(np.transpose(t_inertial_to_body(step)),s_b)
    s_x.append(temp[0])
    s_y.append(temp[1])
    s_z.append(temp[2])

fig, ax = plt.subplots(3, sharex=True)
ax[0].plot(s_x)
ax[0].set_ylabel("x")
ax[1].plot(s_y)
ax[1].set_ylabel("y")
ax[2].plot(s_z)
ax[2].set_ylabel("z")
plt.suptitle("s_b in intertial frame")

plt.show()
