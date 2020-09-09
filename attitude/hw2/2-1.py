import numpy as np
from scipy.integrate import ode
import matplotlib.pyplot as plt

v_b_0 = np.multiply(2 * np.pi / 100, [10, 1, 0])
J = np.multiply(np.identity(3), [100, 60, 60])
J_inv = np.linalg.inv(J)
dv_b_0 = -1 * np.matmul(J_inv, np.cross(v_b_0, np.matmul(J, v_b_0)))
# Y_0 = np.concatenate([v_b_0, dv_b_0], axis=0)
Y_0 = v_b_0
T0 = 0
dT = 1
tF = 1801


def v_b_dot(t, Y):
    # dY=np.empty(3)
    dY = -1 * np.matmul(J_inv, np.cross(Y, np.matmul(J, Y)))
    return dY


def derivFcn(t, Y):
    return v_b_dot(t, Y)


rv = ode(derivFcn)
rv.set_integrator('dopri5', rtol=1e-10, atol=1e-20)
rv.set_initial_value(Y_0, T0)
output = []
output.append(np.insert(Y_0, 0, T0))
while rv.successful() and rv.t < tF:  # rv.successful() and
    rv.integrate(rv.t + dT)
    output.append(np.insert(rv.y, 0, rv.t))
result = np.empty([np.shape(output)[0] - 1, 3])
for index in range(np.shape(output)[0] - 1):
    result[index, 0] = output[index][1]
    result[index, 1] = output[index][2]
    result[index, 2] = output[index][3]

print(result[-1, :])

fig, ax = plt.subplots(3, sharex=True)
ax[0].plot(result[:, 0])
ax[0].set_ylabel("x")
ax[1].plot(result[:, 1])
ax[1].set_ylabel("y")
ax[2].plot(result[:, 2])
ax[2].set_ylabel("z")
plt.suptitle("v_b propogated for 1800 time steps")

plt.show()
