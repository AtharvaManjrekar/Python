import math as m
m.pow(20,2)
m.sqrt(144)
print("The answer of pow(20,2) is: ",m.pow(20,2))
print("The answer of sqrt(144) is:",m.sqrt(144))
print("Now using pi function ")
def area_of_circle(r):
    print("Enter the value of radius:",r)
    area = m.pi*r*r
    print("Area of circle is :",area)
    return 0
area_of_circle(10)