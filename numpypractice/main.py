import numpy as np


# #array
# a= np.array([1,2,3])
# print(a)
#
# #2d array
# b = np.array([[4.3,2.7,5.5],[4.3,2.3,9.0]])
# print(b)
#
# #get the dimension
# print(a.ndim)
# print(b.ndim)
#
# #get shape
# print(a.shape)
# print(b.shape)
#
# #get datatpye
# print(a.dtype)
# print(b.dtype)
#
# #get size
# print(a.itemsize)
# print(b.itemsize)
#
a = np.array([[3,6,12,24,2,4],[9,42,22,17,5,1]])
#get specific element [r,c]
print(a[1,4])

#get first row
print(a[0,:])
#get third col
print(a[:,2])

#getting a little more fancy [startindex:endindex:stepsize]
print(a[0,1:6:2])

# 3d array
b = np.array([[[1,2],[3,4],[5,6]]])

#get specific element - go outside in
print(b[0,1,1])