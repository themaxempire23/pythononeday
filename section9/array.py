# How to use array module in python

import array as arr

my_array = arr.array('i', [10, 99, 80, 46, 32, 20, 12])
print(my_array) # Displaying all elements in the list
print(my_array[4]) # Displaying the 5 element in the list


# creating for loop to display all elements in the array
for i in my_array:
    print(i)