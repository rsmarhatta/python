
# Python3 code to iterate over a list
list = [1, 3, 5, 7, 9]

# Using list comprehension
[print(list[i]) for i in range(len(list)) if i%2==0]