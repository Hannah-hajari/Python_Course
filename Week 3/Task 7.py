import numpy as np

pos_color_dtype = np.dtype([
    ('position', [('x', int), ('y', int)]),
    ('color', [('r', int), ('g', int), ('b', int)])
])

structured_arr = np.array([((10, 20), (255, 0, 0)), ((30, 40), (0, 255, 0))], dtype=pos_color_dtype)

print("Structured Array:\n", structured_arr)
print("Position of first element:", structured_arr['position'][0])
print("Color of second element:", structured_arr['color'][1])