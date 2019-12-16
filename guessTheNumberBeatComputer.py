#guessTheNumberBeatComputer.py
cguess  = 0
unumber = 0
name = ""
name = input("Name please:")
print  ("Welcome",name +",","enter a number to have the computer guess.")
unumber = int(input("Please enter a number 1-100:"))
if unumber >=1 and unumber <= 100:
    print("This number is accepted")
else:
    print("Incorrect number. Please restart this program")
    
