import numpy as np

a = np.array([1,2,3])   # 1D array
print(a)

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])    # 2D array
print(b)

# Get dimension
print(a.ndim)
print(b.ndim)

# Get Shape
print(b.shape)

# Get Type
print(a.dtype)

c = np.array([4,5,6], dtype ='int16')   # Specifying array size in bits
print(c.dtype)

# Get size in bytes
print(a.itemsize)   

# Get number of elements
print(a.size)