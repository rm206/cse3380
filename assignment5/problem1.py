import numpy as np
import sympy as sp

# Setting up A and b
A = np.array([[3, 8, -5],
              [3, -6, -7],
              [3, 4, 2]])
b = np.array([[-1],
              [-1],
              [3]])

# a)
rrefA = np.array(sp.Matrix(A))

# b)
colSpaceA = np.array(sp.Matrix(A).columnspace())

# c)
X = np.linalg.inv(A) @ b

# d)
nulA = np.array(sp.Matrix(A).nullspace())