# U2M3Project_McDanielCarson.py

def wordlist():
    print("Number of charaters is",number,)
    print("Turning qoute into separate words")
    for qoute1 in qoute:
        print(qoute1)
    print("Done!")
   
qoute = input("Enter a qoute (\""" are not required):")
number = len(qoute)
print("Your qoute is", number, "charater(s) long")
if number > 10:
    print("Number of charaters is vaild. Please Wait",wordlist())
elif number <10:
    print("Since your quote is",number, "charater(s) long the word will now be lowercased")
    print(qoute.lower())
print("Thanks for using this program")

