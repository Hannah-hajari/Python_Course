import numpy as np

def generate_integers():
    for i in range(10):
        yield i

arr = np.fromiter(generate_integers(), dtype=int)
print(arr)