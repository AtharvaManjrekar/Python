if __name__ == '__main__':
    print("Now we will create a list")
    harsh = ["Atharva","Ananya","Anushka","Arushi","Ayush","Siddhik","Vedant","Manthan"]
    print("We have created a list:",harsh)
    print("Now we will access the 4th element from list & it is: ",harsh[5])
    harsh[2]="Parth"
    print(harsh)
    print("We will delete",harsh[2],"From the list:")
    harsh.remove(harsh[2])
    print("Result after deleting the second element:",harsh)
    print("The total length of our list is:",len(harsh))