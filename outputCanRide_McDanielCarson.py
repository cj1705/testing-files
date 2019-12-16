# outputCanRide_McDanielCarson.py

# Initialize variables
firstName = ""
lastName = ""
height = 0

# Input users information
firstName = input("What is your first name?")
lastName = input("What is your last name?")
height = int(input('What is your height? (ex 54")'))

# Allowed user to review input
print(' is this the correct information?', firstName, lastName, height ,"in")
print("If not then restart this program")
print()



# height requirement for coasters
if height <= 42 :
    print("You're too short for most kiddie rides.")

elif  height >= 52 :
    print("You're too tall for most kiddie rides.")

else :
    print("You are able to ride some kiddie rides.")
    
# Height requirement for kiddie rides
if height <= 48 :
     print("You're tall enough to ride some rollercoasters.")
#elif height <= 54 :
    #print("You're tall enough to ride some rollercoasters.")
elif height >=78 :
     print("You are too tall for most rollercoasters.")
#elif  height >=80 :
    #print("You are too tall for most rollercoasters.")
else :
    print("You're tall enough to ride some rollercoasters")

   

# print empty line
print()


# print empty line
print()

#saying thank you
print("Thank's for using this program!")

 
