import numpy as np

arr = np.array([1.5, 2.3, 5.8, -3.2, 4.1])

print("1. np.trunc:", np.trunc(arr))

print("2. astype(int):", arr.astype(int))

print("3. np.floor:", np.floor(arr))

print("4. arr - arr % 1:", arr - arr % 1)

print("5. np.modf:", np.modf(arr)[1])