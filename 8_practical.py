import math as m
def area_of_circle(r):
    print("This function will remove area of circle")
    print("Enter the value of radius:",r)
    area = m.pi * r * r
    print("The area of circle is:",area)
    return 0
area_of_circle(10)

# finding even number
def num_getter(num):
    print("Enter the number:",num)
    if(num%2==0):
        print("The entered number is even.")
    else:
        print("The entered number is odd.")
    return 0
num_getter(4)
