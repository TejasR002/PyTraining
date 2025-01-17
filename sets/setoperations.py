emp = { "tejas","tanisha","rohan","prit","pratham"}
nums = { 1,3,4,45,6}
emp.add("saubhagya")
print(emp)
intern = emp.copy()
print(intern)

p_emp= {"tanisha","rohan","tejas","pratham"}

outerliar = emp - p_emp
print(outerliar)

#emp-=p_emp
#print(emp)

outerliar.discard("prit")
print(outerliar)


#intersection 

print(emp & p_emp)

#disjoint 

if(emp.isdisjoint(nums)):
    print("yes it is disjoint")
else: 
    print("Nope")


#subset 

if(p_emp<=emp):
    print("subset che ")
else:
    print("subset nathi")
print(emp)
#pop
def kick(s):
    s.pop()
    return s


x = kick(emp)
print(x)





