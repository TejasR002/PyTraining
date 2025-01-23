import datetime

x = datetime.datetime.now()
print(x)
print(x.date())
print(x.strftime("%B"))

k = datetime.datetime(2020, 5, 17)
print(k)

# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string: