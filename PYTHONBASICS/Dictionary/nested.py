myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


print(myfamily["child1"]["name"])

for member,child in myfamily.items():
    print(member)
    for c in child:
        print(f"{member}:{child[c]}")