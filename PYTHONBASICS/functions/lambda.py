
# t = lambda t: t + 10
# print(t(10))


# x = lambda x,y : x*y
# m = int(input("enter m"))
# n = int(input("enter n"))
# print(x(m,n))

def myfunc(x):
    return lambda k : k*x

doubler = myfunc(2)
print(doubler(10))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))