import numpy as np
matrix = np.random.random((5, 5))

row_means = matrix.mean(axis=1, keepdims=True)
normalized_matrix = matrix - row_means
print("Matrix after subtracting row means:\n", normalized_matrix)