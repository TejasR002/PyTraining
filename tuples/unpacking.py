#tuple unpacking

#  * astricks  make the list 

tupe = ("india","russia","USA","jordan","canada")

(east,north,*west) = tupe

print(north)
print(east)
print(west)


(a,b,c,d,e) = tupe

print(a + b )
print (c + d )

country = ("russia","switzerland","swiden","britan","atlantis","india","zimbave","jordan","ukrain")
(oil,money,*miletary,manpower,petrolium) =  country
print(manpower)
print(oil)
print(money)
print(miletary)
print(petrolium)
