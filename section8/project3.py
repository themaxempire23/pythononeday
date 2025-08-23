"""
This Python tool provides various string manipulation operations like reversing a string, converting it to uppercase or lowercase, counting vowels, and more. It's ideal for practicing Python's string functions.
"""

# Project 3 code:

# String Manipulation Tool
def string_operations(text):
    print("Reversed Text: ", text[::-1])
    print("Uppercase: ", text.upper())
    print("Lowercase: ", text.lower())
    print("Vowels Count: ", sum(1 for char in text if char.lower() in 'aeiou'))
 
# Input from user
user_input = input("Enter a string: ")
 
# Perform string operations
string_operations(user_input)