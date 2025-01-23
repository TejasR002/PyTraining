f = open("demo.txt","r")
print(f.readline())
print(f.read(10))
print("-----------------------------------------------------")
print()

for x in f:
    print(x)
    
f.close()r