#total_cost_McDanielCarson.py
code = ""
choice = ""
amount = 0
total =0
print(                                       "Welcome")
choice = input("Before we start do you have a discount code? y/n:")
if choice  =="y":
    print("You will be asked for the code at the end")
else:
     print("you will not be asked for a code")
while choice !="Done":
   amount = int(input("Please enter the cost of each item. When you are finished type 0:"))
   total = total + amount
   if amount == 0:
       if choice == "y":
           code = input("What is your code")
           if code =="F10":
                total = total *  0.10
                print("You will get 10% off your total")
              
            
           elif code == "E15":
                total = total *  0.10
                print("You will get 10% off your total")
                print("Your new total is " , total , "$")
           elif amount >100:
                print(" Write down this new code for 10% off :E44")
           else:
                print("You total has to be over 100$ to get a new code")
                quit()
       else:
            print("your total is", total,  "$")
            quit()

            
print("Thanks for using this program")
                    
        

    
