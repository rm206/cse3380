import numpy as np
import matplotlib.pyplot as plt

dataset = np.loadtxt("dataset2.txt")
a = dataset[:, 0]
b = dataset[:, 1]

A = np.vstack([a, np.ones(len(a))]).T
m, c = np.linalg.lstsq(A, b, rcond=None)[0]

plt.plot(a, b, 'o', label='Original data', markersize=2)
plt.plot(a, m*a + c, 'r', label='Fitted line')
plt.legend()
plt.show()