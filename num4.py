import numpy as np
values = [1, 7, 13, 105]
array = np.array(values)
memory_size = array.nbytes
print("Array:", array)
print("Memory size occupied by the array:", memory_size, "bytes")