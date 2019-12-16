# outputNameAge_McDanielCarson_9-20-19.py")
# Created Carson McDaniel on 9/20/2019")
# This file will ask the user for their first name, last name, and age, and then informs the user if they are too old for high school."

# initialize variables
# camelCase variable names
firstName = ""
lastName = ""
age = 0

# Asked human for input
firstname = input("What is your first name?")
lastname = input("What is your last name?")
age = int(input("What is your age?"))

# Allowed human to review input
print("Is this the correct information?",firstname, lastname, age)
print("if any information is wrong just restart the program")

# Made high school decision based on input
if  age> 18 :
    print("You're too old for high school.")
else :
    print("You're not too old for high school.")

# Tell human thank you
print("Thanks for using this program.")

