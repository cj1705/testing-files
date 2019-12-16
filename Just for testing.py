size_num = "8 9 10"
size = "8"
if size.isdigit() == False:
                print("invaild")


elif int(size) <8:
                print("Size is too low")
elif size in size_num:
                print("Size is recored")

else:
     print("Size is too high")
