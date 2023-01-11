# creating a tuple
print("Creating a tuple.")
tup = (100,"Atharva",50.30,'Rahul')
print("Tuple created:",tup)

# accessing a tuple
print("The value at 2nd index of tuple is:",tup[2])
print("The value at 1st index of tuple is:",tup[1])

# updating a tuple
dn = ("Mumbai",)
c = dn +tup
print("The new tuple is:",c)

# deleting a tuple
del tup
print("Tuple deleted sucessfully")
print(tup)