print("Now we will be  using try and except block.")
try:
    a = 50/0
except ZeroDivisionError:
      print("You cannot divide a number by 0 ")
      print("exception handled properly...")
else:
     print("division successful")

     