import numpy as np
arr = np.ones((16, 16))

block_sum = arr.reshape(4, 4, 4, 4).sum(axis=(1, 3))
print("Block sum shape (4x4):\n", block_sum)