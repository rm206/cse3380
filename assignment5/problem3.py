'''
[[2b+3c],   = a[[0], + b[[2],  + c[[3],  = (a@v1) + (b@v2) + (c@v3)         
 [a+b-2c],      [1],     [1],      [-2],
 [4a+b],        [4],     [1],      [0],
 [3a-b-c]]      [3]]     [-1]]     [-1]]

 Create a matrix v = [v1 v2 v3]
 Call the sympy.Matrix.rref function on v and find the length of the tuple containing
 the number of pivot columns. 
 The length will be the dimension and the corresponding columns will be the basis.
'''

import sympy as sp
import numpy as np

v1 = sp.Matrix([[0],
                [1],
                [4],
                [3]])
v2 = sp.Matrix([[2],
                [1],
                [1],
                [-1]])
v3 = sp.Matrix([[3],
                [-2],
                [0],
                [-1]])

v = sp.Matrix([[v1, v2, v3]])

return_tuple = v.rref()[1]

print(f"Dimension = {len(return_tuple)}")
print("Basis vectors : ")
for curr in return_tuple:
    print(np.array(v.col(curr)))