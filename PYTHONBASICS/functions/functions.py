

def func1(name,age):#only two arguments are accepted ,           name and age are parameters 
    print(f"Hey {name}! you are {age} years old")

func1("prit",20) # prit and 20 are arguments 


'''
From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
'''

def func2(*args):  # multiple arguments are accepted
    for i in args:
        print(i)

func2("Harsh","amisha","pruthvi","ritu","janmy","silchar")


#ARBITARY KEYWORD ARGUMENTS


def arb_function(**targs):
    print("First Name: " + targs["fname"] + "\nSurname: " + targs["sname"])

arb_function( fname="Saubhagya",sname= "Vish", age = 21)


#default in funciton 
def my_country(country = "india"):
    print("my country is ",country)

my_country("switzerland")
my_country()


#return values
def square(x):
    return x*x
#t = int(input("enter number: "))
t = 5
print(square(t))


#positional only arguments

def myfunc(x,/):
    print(x*x)
myfunc(6)


#keyword only arguments
def yfunc(*,x):
    print(x*x*x)
yfunc( x = 8)



#Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

def my_function1(a, b, /, *, c, d):
  print(a + b + c + d)

my_function1(8, 6, c = 4, d = 2)