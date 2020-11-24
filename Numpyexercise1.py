# Write a NumPy program to test whether none of the elements of a given array is zero

import numpy as np


# print(b)
def findNumberIndex(array, x):
    b = np.count_nonzero(array)
    return [(index) for (index, el) in enumerate(array) if el == x]
    print(l)
    if len(array) - b == 0:
        print("array does not have a zero value")
    else:
        print(f"array has {len(array)-b} zero values")


a = np.array([1, 2, 3, 4, 5, 1])
c = np.array([1, 0, np.nan, np.inf])
result = findNumberIndex(a, 0)
print(result)
# print(np.all(a))
# np.any(a)
print(np.isnan(c))

print(np.allclose([1e10, 1e-7], [1.00001e10, 1e-8]))
