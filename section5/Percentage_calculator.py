"""
This Python program calculates the percentage of a given number.
Users will input the total value and the obtained value, and the program will compute the percentage based on these inputs.
"""

# My Goal: User Input handling


def calculate_percentage(obtain, total):
    percentage = (obtain / total) * 100
    return percentage

# Input from user 
obtained_marks = float(input("Enter obtained marks: "))
total_marks = float(input("Enter total marks: "))

#Calculating percentage
result = calculate_percentage(obtained_marks, total_marks)

print(f"Your percentage is: {result}%")