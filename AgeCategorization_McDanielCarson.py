#AgeCategorization_McDanielCarson.py
age = 0
name = ""

name= input("What is your name")
age = int(input("What is your age"))

if age >=0:
    if age <=2:
        print("You fall in the baby category")            
    elif age >=3 and age <= 10:
        print("You fall in the child category")
        
    elif age >=11 and age <= 12:
        print("You fall in the pre-teen category")
    elif age >=13 and age <= 19:
      print("You fall in the teenager category")
    elif age >=20 and age <= 66:
       print("You fall in the adult category")
    elif age >=99 and age <= 998:
        print("You fall in the Elderly category")
    elif age == 999:
        print("Quitting...")
        quit()
    else:
        print("Incorrect number")

                                      
                                      

