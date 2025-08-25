"""
Title: Character Counter in a String
Description:
This tool takes a string input from the user and counts the number of occurrences of each character in the string, helping the learner understand loops, dictionaries, and string iteration.

Skills Required:

- Dictionary usage

- Loops (for)

- String traversal

- Using the .get() method of dictionary



Algorithm(Pseudocode):

1. Get input string from the user.

2. Initialize an empty dictionary to store character counts.

3. Loop through each character in the string.

4. If character is already in dictionary, increment its count.

5. Otherwise, add it to the dictionary with count 1.

6. Print the character counts.
"""


# Character Counter in a String
user_input = input("Enter a string: ")
char_count = {}
 
for char in user_input:
    char_count[char] = char_count.get(char, 0) + 1
 
print("Character counts:")
for char, count in char_count.items():
    print(f"'{char}': {count}")