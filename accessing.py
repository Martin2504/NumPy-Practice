import numpy as np

# Accessing specific elements, rows, colums, ext.

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])    # 2x7
print(a)
print(a.shape)

# Get specific elemet
print(a[1, 5])
print(a[1, -2])

# Get specific row
print(a[0, :])

# Get specific column
print(a[:, 2])

# Getting a little more fancy [startindex:endindex:stepsize]
print(a[0, 1:6:2])

# Change something (13 to 20)
a[1, 5] = 20
print(a)

# Change a whole column
a[:, 2] = 5 # All numbers become 5 in this column
print(a)