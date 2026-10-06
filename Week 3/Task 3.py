import numpy as np
arr = np.random.random((5, 5))

normalized_arr = (arr - arr.mean()) / arr.std()
print("Normalized Matrix:\n", normalized_arr)