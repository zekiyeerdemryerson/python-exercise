import numpy as np

a = np.array([2, 1, 3, 4, 5, 6, np.nan])
b = np.array([1.1, 2.1, 3.1, 4.1, 5.1, np.nan])

# print(np.allclose(a, b, atol=0.1, equal_nan=True))

# print(np.greater(a,b))
test = np.array(["a"])
print(test.size, test.size * test.itemsize)
print(test.size, test.nbyte)
