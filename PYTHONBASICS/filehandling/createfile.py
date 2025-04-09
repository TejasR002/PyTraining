f = open("create3.txt","x")
f.write("file created using  x mode !")
f.close()

f= open("create3.txt","r")
print(f.read())