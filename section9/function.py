# Function ->  A block of code performs a specific task
# Functions are useful because they allow you to reuse code
#                                 - make programs more efficient and easier to read.

""" Mastering functions

1. know how to create a function
2. know how to call a function

syntax structure:

def function_name(parameter1, parameter2,...)
  
    # function body (where you write your code)
    # Code to perform the task

    return result



 Function components:
 - a function name
 - parameters (which are optional)   
 - function body
 - Return value
"""


# Example 1:
# A test function:

def test1():
    print("Testing function")

# calling the function
test1()    


# Adding other code to the function

# Example 2:

def test():
    a = 10
    c = 20
    result = c - a
    print("Testing adding numbers together in a function")
    print(str(result) +  "You are doing great!")
    print("your results is: ", result)
    # Notice no return statemnet used here
# calling the function
test() 
 
# Example: 3

def sum(x, y):
    add = x + y
    return add

a = int(input("Enter x value: "))
b = int(input("Enter y value: "))

print(sum(a,b))
