import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1, -2], [-4, 1]])

eigvalues = np.linalg.eig(a)[0]
print("Eigen values = ", eigvalues)

plt.quiver([0, 0], [0, 0],
           [1, -4], [-2, 1],
           angles='xy',
           scale_units='xy',
           scale=1,
           color='r',
           label="Columns of A")
plt.quiver([0, 0], [0, 0],
           np.linalg.eig(a)[1][:, 0],
           np.linalg.eig(a)[1][:, 1],
           angles='xy',
           scale_units='xy',
           scale=1,
           color = 'g',
           label = "Eigen vectors")

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.legend()
plt.show()