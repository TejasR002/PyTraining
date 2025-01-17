a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#short hand if 
if a > b: print("a is greater than b")

#short hand if else

a = 2
b = 330
print("A") if a > b else print("B")
#multiple conditional statement
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")