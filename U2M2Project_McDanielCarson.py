# U2M2Project_McDanielCarson.py

list1 =""
list2 = ""
list3 = ""
item = ""

item = input ("Enter a item on any of the lists:")
list1 = ['Hotel', 'Motel', 'House']
list2 = ['Hard Drive', 'SSD', 'Monitor', 'Desktop']
list3 = ['rain', 'flood', 'thunder']

def list_o_matic():
    print("This program will show the list(s) that this item is in.")
    print()
    if item in list1:
        print()
        print(list1,"List 1")
     
    else:
      
        print("Not in list 1")
        print()
    if item in list2:
        print(list2,"List 2")
        print()
    else:
       
        print("not in list 2")
        print()

    if item in list3:
        print(list3,"List 3")
        print()
        
    else:
        print("Not in list 3")
        print()
    print("Thinks for using this program")
    
    
    


if item in list1:
    list_o_matic()
elif item in list2:
    list_o_matic()
elif item in list3:
    list_o_matic()
else:
    print("Item is not on the list")


