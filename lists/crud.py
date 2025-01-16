lst = ["india","japan","columbia"]

for l in lst:
    print(l)

print(lst[1])

lst.append("china") #insert at last  position
print(lst)

lst.remove("japan")
print(lst)


list1 = ["abc", 34, True, 40, "male"]
print(type(list1))

thislist = list(("apple", "banana", "cherry")) # the double round-brackets used for making list 
print(thislist)

thislist.insert(3,"mango") # inserts at specific position
print(thislist)


vegies = [ "potato","tomato","frenich"]
thislist.extend(vegies) # merge two list or any two iterables  list and set, list and array, list and tuple .
print(thislist)
