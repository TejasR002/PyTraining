f = open("writemode.txt","w")
f.write("The file is being written in write mode where overwritting is happening") 
f.close()

t = open("writemode.txt","r")
print(t.read())
