# String -> A sequnce of characters

name = 'Tim Smithon'
print(name[9]) # Displaying the 9th character in the string


# Slicing
print(name[0:6])

# Examples 2: Conatination -> adding string together / joining string strings together end to end e.g 'snow' and 'ball' reslut: 'snowball'

first_name = 'Alex'
last_name = 'Goldin'

full_name = first_name + " " + last_name # " " adds a spce for the output
print(full_name)

# Formating a string
name = "Hilary"
age = 30

string = 'My name is {} and I am {} years old!'.format(name, age)
print(string)
