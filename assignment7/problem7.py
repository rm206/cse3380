import numpy as np
import copy

# a. Taking n and m as 5
n = 5
m = 5
X = np.random.rand(n, m)
print("Generated X : \n\n", X)
print()

# b.
xtx_eig_values, xtx_eig_vectors = np.linalg.eig(X.T @ X)
print("X^TX eigenvalues : \n\n", xtx_eig_values)
print()
print("X^TX eigenvectors : \n\n", xtx_eig_vectors)
print()

# c.
eig_vectors_projected = X @ xtx_eig_vectors
eig_vectors_projected_normalized = copy.copy(eig_vectors_projected)
for i in range(m):
    eig_vectors_projected_normalized[:, i] = eig_vectors_projected[:, i]/np.linalg.norm(eig_vectors_projected[:, i])
print("Projected eigenvectors : \n\n", eig_vectors_projected)
print()
print("Projected eigenvectors normalized: \n\n", eig_vectors_projected_normalized)
print()

# d.
u, s, vh = np.linalg.svd(X, full_matrices=False)

# e.
print("U : \n\n", u)
'''
The absolute values in the columns of projected normalized eigenvectors and U are the same
and differ only by a negative sign in some columns and is exactly the same in other columns
'''