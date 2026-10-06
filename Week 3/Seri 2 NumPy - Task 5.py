import numpy as np

arr = np.array([[1, 5, 3],
                [4, 2, 6],
                [7, 8, 0]])
n = 1
sorted_arr = arr[arr[:, n].argsort()]
print("Sorted by column", n, ":\n", sorted_arr)