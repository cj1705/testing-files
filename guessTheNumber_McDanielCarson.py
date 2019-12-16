#guessTheNumber_McDanielCarson.py
from random import randint
guess = ""
guessCount = 0
name = input("What is your name")

print("Hello",name + "," , "I would like to play a game")

myNumber = randint(1 , 50)


diff = input("Easy, Hard, or Crazy:")

if (diff == "Easy" or diff =="easy"):
    print("I'm thinking of a number 1-50 you have 20 tries to guess it")
    while guess != myNumber and guessCount < 20:
        guessCount +=1
        guess =int(input("Go ahead and guess"))
        if guess > myNumber:
            print("Guess lower")

        elif guess < myNumber:
            print("Guess higher")
        else:
            print("You guessed it")
        print(" You have guessed",guessCount,"Times out of 20")

    print("You are all out of guesses")
    quit()
    
elif (diff == "Hard" or diff =="hard"):
     print("I'm thinking of a number 1-50 you have 10 tries to guess it")
     while guess != myNumber and guessCount < 10:
        guessCount +=1
        guess =int(input("Go ahead and guess"))
        if guess > myNumber:
            print("Guess lower")

        elif guess < myNumber:
            print("Guess higher")
        else:
            print("You guessed it")
        print(" You have guessed",guessCount,"Times out of 10")

        print("You are all out of guesses")
    
elif (diff == "Crazy" or diff =="crazy"):
     print("I'm thinking of a number 1-50 you have 5 tries to guess it")
     while guess != myNumber and guessCount < 5:
        guessCount +=1
        guess =int(input("Go ahead and guess"))
        print(" You have guessed",guessCount,"Times out of 5")
        if guess > myNumber:
            print("The numer was lower")

        elif guess < myNumber:
            print("The number was Higher")
        else:
            print("You guessed it")
         

     print("You are all out of guesses")
    

