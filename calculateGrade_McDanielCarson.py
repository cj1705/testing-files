# output_calculategrade_McDanielCarson_9-26-19.py

# Initialize variables

firstName = ""
grade = 0.0

# Input from user
firstName = input("What is your first name")
grade = int(input("Please enter your score(ex 80)"))


# Confirmation
print(" Is this correct?",firstName, grade,"%")

# Selection
if grade > 90 :
    print("You have got a A")
elif grade >= 80 :
    print("You have got a B")
elif grade >=70 :
    print("You have got a C")
elif grade > 60 :
    print("You have got a D")
elif grade < 60 :
    print("You have got a E")

# Goodbye 
print("Thanks for using this program")




