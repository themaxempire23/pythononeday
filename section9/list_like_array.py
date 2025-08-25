# Array is a built in data_type

# Array of F1 teams:

arr = ['Redbull', 'Meclaren', 'Mercedez-benz', 'Alpine', 'Redbull Racing']
print(arr) #Accessing the array

# Displaying an element based on their position in the array list
print(arr[4])

# adding a new element
arr.append('Audi')
print(arr)

# removing an element
arr.remove('Alpine')
print(arr)

# Sorting the elements in order/any order we prefer
arr.sort()
print(arr)

# Modifying the array list
# Replacing an existing element with a new one
arr[2] = 'Aston Martin'
print(arr)