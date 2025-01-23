#create dictionary 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#access variable

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#no duplicate values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdict))

#constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


#access using get()

print(thisdict.get("name"))

#get list of keys using keys()

print(thisdict.keys())

#get the values in the dictionary

print(thisdict.values())

#get the items of the dictionary in the tuple list 
print(thisdict.items())

#UPDATE DICTIONARY 


thisdict.update({"state":"arizona"})
print(thisdict)

# Delete the items
print("before popitem operation ",thisdict)
thisdict.popitem()   # it removes the last item from the dictionary
print("after popitem operation",thisdict)
thisdict.pop("name") # it removes specific item from the dictionary
print(thisdict)


thisdict.clear()# deletes the data of the dictionary
print(thisdict)
del thisdict #deltes the entire dictionary
print(thisdict)
