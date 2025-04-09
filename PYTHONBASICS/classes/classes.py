#A Class is like an object constructor, or a "blueprint" for creating objects.

class MyClass:
  x = 5

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(p1)  # prints obejct addresh in hexadecimal  because _str__() function is not available 



class students:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    def __str__(self):
      return f"{self.name} -> {self.age}"

s1 = students("harsh",54)
print(s1) # prints the obejct parameters   cause __str__() function is  inside the class