

import numpy as np
import random
#array s 0
print(np.zeros((2,3)))

#arrays as 1
print(np.ones((5,3)))

#any number
print(np.full((2,2),99))

#random decimals
print(np.random.rand(4,2))

#random int
print(np.random.randint(5,30, size = (3,3)))

#identity matrix
print(np.identity(5))

#array repeating itself
arr1= np.array([[1,2,3]])
arr2 = np.repeat(arr1,5,axis=0)
print(arr2)

#practice array
output = np.ones((5,5))
zero = np.zeros((3,3))
zero[1,1]=9
output[1:4,1:4]= zero
print(output)

#vertically stacking
v1 = np.array([1,2,3,4])
v2 = np.array([55,66,777,88])
print(np.vstack([v1,v2,v1]))

#horizontal stacking
v3 = np.array([1,2,3,4])
v4 = np.array([55,66,777,88])
print(np.hstack([v4,v3,v3]))