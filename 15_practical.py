dn = open("gpm.txt")
with open("gpm.txt") as dn:
     print("Now we will read the data from that file")
     content = dn.read()
     print(content)
     dn.close()