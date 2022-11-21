import scipy as sp
import numpy as np

A = np.array([[1, 0, 4], [-2, 3, -2], [-2, 0, 6]])
Q, R = sp.linalg.qr(A)

print("Q : ", Q, sep = "\n\n", end = "\n\n")
print("R : ", R, sep = "\n\n")