# Write a Python program to demonstrate the use of if and if else.

a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
if(a>b):
    print("The value of a is greater than b ")
elif(a<b):
    print("The value of b is greater than a ")
elif(a==b):
    print("Both values are similar ")
else:
    print("Invalid value")