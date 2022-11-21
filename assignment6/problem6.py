import numpy as np
import matplotlib.pyplot as plt

dataset = np.loadtxt("dataset2.txt")
a = dataset[:, 0]
b = dataset[:, 1]

A = np.vstack([a, np.ones(len(a))]).T
m, c = np.linalg.lstsq(A, b, rcond=None)[0]

xn = a
popt = np.polyfit(a, b, 2)
yn = np.polyval(popt, xn)

plt.plot(a, b, 'o', label='Original data', markersize=2)
plt.plot(a, m*a + c, 'red', label="Linear fit")
plt.plot(xn, yn, 'black', label = "Polynomial fit")
plt.legend()
plt.show()