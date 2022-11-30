import numpy as np
import matplotlib.pyplot as plt

dataset = np.loadtxt("dataset2.txt")
a = dataset[:, 0]
b = dataset[:, 1]

A = np.vstack([a, np.ones(len(a))]).T
m, c = np.linalg.lstsq(A, b, rcond=None)[0]

popt2 = np.polyfit(a, b, 2)
yn2 = np.polyval(popt2, a)

popt3 = np.polyfit(a, b, 3)
yn3 = np.polyval(popt3, a)

popt4 = np.polyfit(a, b, 4)
yn4 = np.polyval(popt4, a)

plt.plot(a, b, 'o', label='Original data', markersize=2)
plt.plot(a, m*a + c, 'red', label="Linear fit")
plt.plot(a, yn2, 'black', label = "Polynomial fit - degree 2")
plt.plot(a, yn3, 'green', label = "Polynomial fit - degree 3")
plt.plot(a, yn4, 'blue', label = "Polynomial fit - degree 4")
plt.legend()
plt.show() 