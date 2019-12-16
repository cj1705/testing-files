#U2M1Project_McDanielCarson.py

word = input("Enter a Quote")
if word.isalpha:
    print(word + "a")
elif word == "":
    print("nothing was typed")
elif word.startswith("h"):
    print(word.capitalize())
