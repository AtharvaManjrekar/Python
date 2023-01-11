def isPalindrome(num):
    string = str(num)
    string2 = string[::-1] # reverses a string
    if(string == string2):
        return 1
    else:
        return -1

c = isPalindrome(121)
print(c)
