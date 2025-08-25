"""
Array Sorting Tool
Description: This Python tool allows you to sort an array of numbers either in ascending or descending order using Python's built-in sorting methods.

Goal: Understanding of arrays (lists in Python)
"""

# Array Sorting Tool
def sort_array(arr, order='asc'):
    if order == 'asc':
        arr.sort()
    else:
        arr.sort(reverse=True)
    return arr
 
# Input from user
arr = list(map(int, input("Enter numbers separated by space: ").split()))
order = input("Enter sorting order (asc/desc): ")
 
# Perform sorting
sorted_array = sort_array(arr, order)
print("Sorted Array:", sorted_array)