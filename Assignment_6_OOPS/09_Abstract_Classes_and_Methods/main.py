#Use the abc module to create an abstract class Shape with an abstract method area().
#  Inherit a class Rectangle that implements area().




from abc import ABC, abstractmethod

#abstracmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
result = Rectangle(3, 5)
print(f"Area of Rectangle: {result.area()}")
