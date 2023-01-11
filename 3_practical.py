# creating a list
print("Now creating a list:")
lst = [101,500,3000,200,5,50,900]
print("Created list is : ",lst)

# accessing a list
print("The value present at 3rd index is: ",lst[3])
print("The value present at 5th index is :",lst[5])
print("We have successfully accessed the above elements.")

# updating a list
lst[6] = 2550
lst[1] = 24
print("List after updation is: ",lst)

# deleting a list
min(lst)
max(lst)
print("The minimum value in list is:",min(lst))
print("The maximum value in list is:",max(lst))

# deleting element from list
lst.remove(lst[0])
print("We have sucessfully deleted an element")
print(lst)