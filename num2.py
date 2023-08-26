import numpy as np

def none_are_zero(arr):
    return np.all(arr != 0)
    
array1 = np.array([1, 2, 3, 4])
array2 = np.array([0, 2, 3, 4])

print("Array 1:", none_are_zero(array1))
print("Array 2:", none_are_zero(array2))