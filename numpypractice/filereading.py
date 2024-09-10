import numpy as np

filedata = np.genfromtxt("data.txt",delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

#Advanced indexing, boolean masking
#check where in filedata the num is greater than 25
print(filedata>25)
print(filedata[filedata>25])

#You can index with a list in numpy
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]])

#check if any value is greater than 25
np.any(filedata>50, axis =0)