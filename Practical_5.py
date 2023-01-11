# try except code
if __name__ == '__main__':
    print("In this code will use try except method.")
    try:
        a = 50/0
    except: ZeroDivisionError
    print("You cannot divide a number by 0")
else:
    print("The division of number is:",a)
