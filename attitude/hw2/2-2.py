import numpy as np
from scipy.integrate import ode
import matplotlib.pyplot as plt

Y_0 = [1, 0]
T0 = 0
dT = 0.1
tF = 10
A = [[0, 1], [-1, 0]]

def u(x):
    return np.multiply(-x, [0.1, 0.01])

def derivFcn(t, Y):
    dY = np.matmul(A, Y)+u(Y[0])
    return dY

rv = ode(derivFcn)
rv.set_integrator('dopri5', rtol=1e-10, atol=1e-20)
rv.set_initial_value(Y_0, T0)
output = []
output.append(np.insert(Y_0, 0, T0))
while rv.successful() and rv.t < tF:  # rv.successful() and
    rv.integrate(rv.t + dT)
    output.append(np.insert(rv.y, 0, rv.t))
result = np.empty([np.shape(output)[0] - 1, 2])
for index in range(np.shape(output)[0] - 1):
    result[index, 0] = output[index][1]
    result[index, 1] = output[index][2]

print(result[-1, :])

tspan = np.arange(T0, 10.1, dT)

fig, ax = plt.subplots(2, sharex=True)
ax[0].plot(tspan, result[:, 0])
ax[0].set_ylabel("x")
ax[1].plot(tspan, result[:, 1])
ax[1].set_ylabel("y")
plt.suptitle("x(t) integrated for 10 seconds")

plt.show()
