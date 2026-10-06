import numpy as np
coords = np.random.random((100, 2))

X = coords[:, np.newaxis, :]
Y = coords[np.newaxis, :, :]
distances = np.sqrt(np.sum((X - Y) ** 2, axis=-1))
print("Distance matrix shape:", distances.shape)