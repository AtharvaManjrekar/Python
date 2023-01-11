age = int(input("Enter your age:"))
if(age>=18):
    print("You can drive a vehicle ")
elif(age>=70):
    print("It is risky to drive a vehicle at this age")
elif(age<18):
    print("You cannot drive a vehicle.")
else:
    print("Enter your correct age:")
