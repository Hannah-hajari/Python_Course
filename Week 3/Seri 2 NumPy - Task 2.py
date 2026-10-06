import numpy as np

A = np.random.randint(0, 10, (3, 3))
B = np.random.randint(0, 10, (3, 3))

are_equal = np.array_equal(A, B)
print("Are A and B equal?", are_equal)