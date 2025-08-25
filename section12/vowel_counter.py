"""
Title: Vowel Counter in a String
Description:
This project asks the user to input a string and then counts how many vowels (a, e, i, o, u) are present in it. It’s a great practice to reinforce concepts of strings, loops, and conditionals.

Skills Required:

- String handling

- For loop

- Conditional statements (if)

- Lowercasing string with .lower() method



Algorithm (Pseudocode):

1. Get input string from the user.

2. Convert the string to lowercase.

3. Initialize a count variable to zero.

4. Loop through each character in the string.

5. If the character is in aeiou, increment the count.

6. Display the total number of vowels.
"""


# Vowel Counter in a String
user_input = input("Enter a string: ")
vowel_count = 0
 
for char in user_input.lower():
    if char in 'aeiou':
        vowel_count += 1
 
print("Total vowels in the string:", vowel_count)