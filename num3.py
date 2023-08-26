import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([3, 2, 1, 4, 6])
greater_than = array1 > array2
greater_equal = array1 >= array2
less_than = array1 < array2
less_equal = array1 <= array2
print("Array 1:", array1)
print("Array 2:", array2)
print("Greater than:", greater_than)
print("Greater than or equal:", greater_equal)
print("Less than:", less_than)
print("Less than or equal:", less_equal)