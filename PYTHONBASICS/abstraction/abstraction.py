from abc import ABC, abstractmethod

class Shape():
    pass
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    

rectangle = Rectangle(10, 5)
print(f"Area: {rectangle.area()}")        # Output: Area: 50
print(f"Perimeter: {rectangle.perimeter()}") 