'''
Python Inheritance

-> Inheritance allows us to define a class that inherits all the methods and properties from another class.

-> Parent class is the class being inherited from, also called base class.

-> Child class is the class that inherits from another class, also called derived class.

'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def name(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("rohan", "dubey")
x.name()


class Student(Person):
  def __init__(self, fname, lname,year):
    super().__init__( fname, lname)
    self.anivarsary = year

  def greet(self):
    print(f"!hello from {self.firstname}")


x = Student("prit","pratham",2028)
print(x.anivarsary)
x.greet()