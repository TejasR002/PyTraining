strs = ["eat","tea","tan","ate","nat","bat"]
# - Output: [["bat"],["nat","tan"],["ate","eat","tea"]

def makedict(strs):
    my_dict = {}
    for x in strs:
        k = list(x)
        t = tuple(sorted(k))
        my_dict[x] = t
    return my_dict
def sortlist(list):
    return lambda s : list.sort()
    
temp = makedict(strs)
#print(temp)
newdict = {}                                                                              
for key,val in temp.items():
    if val in newdict:
        newdict[val].append(key)
    else:
        newdict[val] = [key]


intermediate = list(newdict.values())
for x in intermediate:
    x.sort()
intermediate.sort(key=len)
print(intermediate)





  






