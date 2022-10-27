import numpy as np

def xBTox(B: np.array, xB: np.array) -> None:
    '''
    Takes a basis matrix and a vector in that basis and prints the vector in standard basis.
    Multiplies the basis matrix B by xB. The result, x, is printed.
    '''
    print(B @ xB)


B = np.array([[0, -4, 6],
              [-1, 0, 6],
              [-1, 0, 3]])

xB = np.array([[-2],
               [6],
               [1]])

xBTox(B, xB)