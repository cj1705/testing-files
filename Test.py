# [ ] build a list (add_animals) using a while loop, stop adding when an empty string is entered
add_animals = []
add_animals = input("Make a list of animals:, ex:sheep,cow")
print("Thanks now lets add more animals to this list")
animals = ["Chimpanzee", "Panther", "Wolf", "Armadillo"]
animals.extend(add_animals)
sorted1 = input("Do you wanted it sorted in reversed order(r) or alphabetical order?(a): ")
if sorted1 =="a":
    animals.sort()
    print(animals)
elif sorted1 =="r":
    animals.reversed()
    print(animals)


