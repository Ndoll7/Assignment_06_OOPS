# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!".
#  Apply it to a class Person.

# Define the class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Apply the decorator to the class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name


p = Person("Alice")
# print(p.name)
print(p.greet())  
