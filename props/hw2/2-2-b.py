import numpy as np
import math as m
import matplotlib.pyplot as plt

tref = np.linspace(917, 1600, num=1000)
tref_b = np.linspace(300, 523, num=1000)
s0 = 0
T1 = 300
T2 = 917.36
T3 = 1600
T4 = 523.24
cp = 1.005

# This is top expo curve
s0 = 0
s1 = cp*m.log(tref[1]/T2)
s_a = np.empty(np.shape(tref))
s_b = np.empty(np.shape(tref))
for step in range(np.size(s_a)):
    if step == 0:
        s_a[step] = s0
        s_b[step] = s0
    elif step == 1:
        s_a[step] = s1
        s_b[step] = s1
    else:
        s_a[step] = cp * m.log(tref[step] / tref[step - 1]) + s_a[step - 1]
        s_b[step] = cp * m.log(tref_b[step] / tref_b[step - 1]) + s_b[step - 1]
plt.plot(s_a, tref)
plt.plot(s_b, tref-617)
plt.vlines(0, 300, 917)
plt.vlines(s_a[-1], 523, 1600)
plt.show()
