import numpy as np

# Initializing different types of arrays.

# All 0s matrix.
a = np.zeros(5)
print(a)
print(np.zeros((2,3,3)))

# All 1s matrix.
print(np.ones((4,2,2)))

# Any other number.
print(np.full((2,2), 99))

# Any other number (full_like)
print(np.full_like(a, 4))       # Replace the 0's with 4's in a. 

# Random decimal numbers matrix. 
print(np.random.rand(4,2))
print(np.random.randint(7, size=(3,3))) # Random int's
print(np.random.random_sample(a.shape)) # Replace the 0's with ramdp, decimals in a. 

# Identity matrix
print(np.identity(3))

# Challenge
output = np.ones((5,5))
z = np.zeros((3,3))
z[1,1] = 9
output[1:4, 1:4] = z
print(output)
