#union  or   |  <- symbol for union of two sets

set1 = { "a","b","c","x"}
set2 = {6,5,4,7,8,9}

print(f"this is set12 -> {set2}")

set4 = set1.union(set2)
set3 = set1 | set2


s3 = {"John", "Elena"}
s4 = {"apple", "bananas", "cherry"}


print(set3)
print(set4)


for i in set3:
    print(i,end="")
print()


s5 = set1.union(set2,s3,s4)
print(s5)


#Update set -> updates the original set ,doesn't return new set


se1 = {1,3,4,5,6}
se2 = { "i","j","k","l"}
se1.update(se2)
print(se1)

#intersection
s6  = set2 & se1
print(s6)
#intersection update -> same as intersection but doesn't create new set , updates the original set.
set2.intersection_update(se1)
print(set2)

#difference 
diffset1 = set2.difference(set1)
print(diffset1)
diffset = set2 - set1
print(diffset)

#difference_update

set2.difference_update(set1)
print(set2)


#symmetric difference ->  gives the (union - intersection)  gives not present in both    operator = " ^ "

print(set2)
print(se1)
sydiffset = set2.symmetric_difference(se1)
print("symmetric difference",sydiffset)
 

s11 = se1 ^ set2
print(s11)
#symmetric differnece update  gives the (union - intersection)  gives not present in both


