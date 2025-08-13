"""This Python program allows users to input their name, then displays a personalized greeting message.
 It’s a simple example of string manipulation in Python"""


def personalised_greeting(name):
    return f"Hello, {name}! Welcome to my application."

#Input from user
user_name = input("Enter your name here: ")

#Generatring and displaying the greeting
greeting = personalised_greeting(user_name)
print(greeting)