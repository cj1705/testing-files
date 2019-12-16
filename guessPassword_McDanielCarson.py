#guessPassword_McDanielCarson.py

quitt  = "a"
while quitt == "a":

    word = "password"
    guess = input("whats the password. q to quit:")
    if guess =="q":
        quitt = "q"
    else:
        print()
    if word =="password":
        print ("You guessed it")
    else:
        print()
