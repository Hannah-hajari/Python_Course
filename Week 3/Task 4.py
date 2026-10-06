import numpy as np
matrix_5x3 = np.ones((5, 3))
matrix_3x2 = np.ones((3, 2))

result_matrix = matrix_5x3 @ matrix_3x2
print("Matrix Product (5x2):\n", result_matrix)