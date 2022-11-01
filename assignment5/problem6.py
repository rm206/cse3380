import numpy as np

def computeL1Loss(u : np.array, v : np.array):
    return np.sum(np.abs(u-v))

def computeL2Loss(u : np.array, v : np.array):
    return np.sum(np.dot(u-v, u-v))

v1 = np.random.rand(5)
v2 = np.random.rand(5)

print("V1 : ", v1)
print("V2 : ", v2)
print("L1 Loss :", computeL1Loss(v1, v2))
print("L2 Loss :", computeL2Loss(v1, v2))