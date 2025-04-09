#alphabatically sorting
thislist = ["orange", "Mango", "kiwi", "Pineapple", "Banana"]
thislist.sort()
print(thislist)

#sort function sorts alphanumerically acending by default 

#decending sorting
nums = [ 2,6,9,62,36,66,76,58,4]
nums.sort(reverse=True)
print(nums)

n = thislist.reverse()
print(n)


thislist.sort(key=str.lower)  # key parameter lets you change the approach for sorting 
print(thislist)


def func(n):
    return abs(n-50)

nums.sort(key=func)
print(nums)
