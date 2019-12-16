# Output_McDanielCarson_lastDayActivity.py
# 9/25/19

# Initialize variables
add = ""
chosenActivity = ""
name = ""
charge = 0

# Greeting
name = input("What is your name?")
print("Hello", name, ", You are about to choose what activity you would to participate in during the last term.")
print("The choices are kayaking (K), paintball(P), zip line(Z), or a choice you have added (A).")
#Line spacing

print()

# Input

chosenActivity = input("Please select a letter.(K,P,Z,A):")

# Selection

if (chosenActivity =="K") or (chosenActivity =="k"):
    charge = charge + 15
    print(" You have selected kayaking.")
    print(" This will cost",charge , "dollars.")

elif  (chosenActivity == "A") or (chosenActivity == "a"):
        add = input("What is your extra choice (Extra choice will cost 25 dollars.)")
        charge = charge + 25
        print("You have selected" , add ,".")
        print(" This will cost",charge , "dollars.")
elif (chosenActivity == "P") or (chosenActivity == "p") :
    print("You have selected paintball")
    charge = charge + 25
    print(" This will cost",charge , "dollars.")
elif (chosenActivity == "Z")  or (chosenActivity == "z") :
    print("You have selected zip line.")
    charge = charge + 35
    print(" This will cost",charge , "dollars.")





else:
    print("You have entered invalid characters. Please restart and enter a valid character.")
    print("You won't be billed.")



# Billing/end
print("You will be billed", charge, "dollars for you're last day activity.") 
    
        
