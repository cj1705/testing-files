# output_baggage_McDanielCarson.py

# initialize veriables
name = ""
bags = 0
bag1 = 0
bag21 = 0
bag22 = 0
bag31 = 0
bag32 = 0
bag33 = 0
charge = 0


# Input
name = input("What is your name?: ")
bags = int(input("How meny bags do you have?:"))

# confirmation
print("Is this correct?" , name, bags, "bags" , )

if bags == 1:
    bag1 = int(input(" how heavy is your bag?:"))

elif bags == 2 :
    bag21 = int(input(" Please enter the weight of one of your bages?"))
    bag22 = int(input("What is the weight of your other bag?"))

elif bags == 3 :
    bag31 = int(input(" Please enter the weight of one of your bages?"))
    bag32 = int(input("What is the weight of your 2nd bag?"))           
    bag33 = int(input("What is the weight of your 3rd bag?"))

else :
    print("You have entered in invalid input this program will now end")

#desiding if bags are overweight
if bag1 >=50:
    print("You will be charged $60.00 for the overweight bag.")
    charge = 60.00
else: 
    charge = 30.00

if bag21 >=50:
    print("You will be charged $30.00 extra for the overweight bag.")
    charge21 = 60.00
else :
    charge21 = 30.00
if bag22>=50:
     print("You will be charged $30.00 extra for the overweight bag.")
     charge22 = 60.00
else :
    charge22 = 30.00

if bag31 >=50 :
    print("You will be charged $30.00 extra for the overweight bag.")
    charge31 = 60.00
else:
    charge31 = 30.00
if bag32 >=50 :
    print("You will be charged $30.00 extra for the overweight bag.")
    charge32 = 60.00
else:
    charge32 = 30.00
    
if bag33 >=50 :
    print("You will be charged $30.00 extra for the overweight bag.")
    charge33 = 60.00
else:
    charge33 = 30.00



if bags== 1:
    print("You will be charged","$",charge,"dollars")

if bags== 2:
    print("You will be charged",charge21 + charge22,"dollars")

if bags== 3:
    print("You will be charged",charge31 + charge32  + charge33,"dollars")

    



    







