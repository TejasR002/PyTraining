class Person:
  def __init__(self, name):
    self.name = name

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("yessu")

p1.myfunc()


#self parameter
'''
The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:
'''

class Persona:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Persona("tim", 26)
p1.myfunc()