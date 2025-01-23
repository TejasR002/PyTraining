#change case 
x = "god"
print(x.upper())
x = input("Enter your name : ")
x = x.upper()
print(f"your name is {x}")


k = "LG"
print(k.lower())


t = "indian"
print(t.replace('a','e'))

#remove white space from begining and end-> strip()

username = input("Enter your username: ")
uname = username.strip()
print(uname)


#SPLIT 

name = input("Enter full name : ")
names = name.split(" ")  # can specify specific separator like comma, space   , @ ,etc.
for n in names:
    print(n)