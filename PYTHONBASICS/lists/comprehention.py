fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


lst = [ x for x in fruits if "e" in x]
print(lst)
list2 = [ x for x in fruits if len(x) > 4 ]
print(list2)
