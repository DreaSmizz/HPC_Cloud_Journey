# INTRO TO PYTHON

# Variables
# Format: Name = value

# Example
age = 30

# If we wanted to show the value we assigned to age on the screen use print statement along with variable name.
print(age)

# Can also just print values directly to screen.  But benefit to using variables is that you can update the value in one place
# without having to worry about updating all over code.
print(35)

# Can also update the value of the variable after declaring initially and it will change.
age = 44
print(age)

# If you want to use a longer variable name, connect them with '_'
friend_age = 40

# Variable name that will never change are written in uppercase.
PI = 3.14159

# Numbers in Python
integer_division = 13 // 5
print(integer_division)
remainder = 13 % 5
print(remainder)

# Python Strings

# Example
my_string = 'Hello, world!'
print(my_string)

string_with_quotes = "Hello, it's me."
# Have to use double quotes on the outside due to the single quote being used on the inside of the string
another_with_quotes = 'He said "You are amazing!" yesterday.'
quotes_with_back_slash = "He said \"You are amazing!\" yesterday."
# This example shows the use of all the same type of quotes, if you want to do this option you have to use '\' or escape
"""
Escaping (putting a backslash in front of a character) is used in Python to remove meaning from a 
character.  In the example above, we remove Python's meaning of "starting or ending a string."

"""

multiline = """Hello, world.

My name is Drea.  Welcome to my program.
"""

print(multiline)

# Python String Formatting

# F strings allow us to print numbers and strings together
age = 34
print(f"You are {age}")

# .formatting
name = "Drea"
# This is much more readable and understandable by future users.  If you leave it blank, anything can be passed in.
final_greeting = "How are you, {name}?"
drea_greeting = final_greeting.format(name=name)
print(drea_greeting)


# Boolean
my_number = 5
user_number = int(input("Enter a number: "))

matches = my_number == user_number

print(my_number == user_number)

# and & or in Python

age = 25

result = age < 18 and age < 65
print(result)

bool(0) # False, zero
bool(13) # True

bool("") # False, empty string
bool("Hello") # True

bool([]) # False, empty list
bool([1, 3, 5]) # True

# Example
default_greeting = "there"
name = input("Enter your name: (optional) ")

user_name = name or default_greeting

print(f"Hello, {user_name}!")

# List
friends = ["Rolf", "Bob", "Anne"]
print(friends[0])

friends_list = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]
print(friends_list[0])

