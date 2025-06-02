🧠 OOP Practice Assignments in Python
Assignment List
Using self:
Create a Book class. Initialize with title and author using self. Add a summary() method to print both.

Using cls:
Build a User class to count the number of users created. Use a class variable and a class method to access the count.

Public Variables/Methods:
Define a Laptop class with a public model attribute and a boot() method. Demonstrate accessing both from outside the class.

Class Variables/Methods:
Create a School class with a class variable for school_code. Add a class method to update the code for all instances.

Static Methods:
Implement a StringUtils class with a static method reverse(s) that returns the reversed string.

Constructors/Destructors:
Design a Session class that prints a message when a session starts (object created) and ends (object deleted).

Access Modifiers:
Make a Customer class with a public name, protected _email, and private __credit_card. Test access levels.

super():
Develop a Vehicle class with make. Inherit Bike from Vehicle, add type, and use super() in the constructor.

Abstract Classes:
Use abc to define an abstract Appliance class with abstract method power_usage(). Inherit Fan and implement it.

Instance Methods:
Write a Cat class with name and color. Add a meow() instance method that prints a message with the cat’s name.

Class Methods:
Create a Ticket class with a class variable tickets_sold. Add a class method to increment this count.

Static Methods:
Build a Geometry class with a static method area_of_circle(radius) returning the area.

Composition:
Define a Battery class and a Phone class. Pass a Battery instance to Phone and access a method of Battery via Phone.

Aggregation:
Make a Team class and a Player class. Store independent Player objects in Team to show aggregation.

MRO & Diamond Inheritance:
Create classes X, Y, Z, W where W inherits from both Y and Z, and both inherit from X. Override a method in Y and Z, and test MRO in W.

Function Decorators:
Write a timer decorator that prints execution time of a function. Apply it to a compute() function.

Class Decorators:
Create a timestamp_class decorator to add a created_at attribute to any class it decorates.

Property Decorators:
Implement a Rectangle class with private _width and _height. Use @property, @setter, and @deleter for area.

callable() & call():
Build a Divider class that takes a divisor and implements __call__() to divide input numbers.

Custom Exception:
Define a NegativeBalanceError and raise it in a withdraw(amount) method if balance goes negative. Handle with try-except.

Custom Iterable:
Create a Fibonacci class that generates Fibonacci numbers up to a limit using __iter__() and __next__().

Polymorphism:
Create a base class Shape with a method draw(). Inherit Circle and Square from Shape and override draw() in each. Demonstrate polymorphic behavior by calling draw() on a list of shapes.

Association:
Make a Doctor class and a Hospital class. Show association by assigning doctors to hospitals, but allow doctors to work at multiple hospitals.

Binary Search Tree:
Create a BinarySearchTree class with methods to insert and search for elements.

Calculator:
Implement a Calculator class with methods for add, subtract, multiply, and divide operations.

📚 Requirements

Standard Python 3+ installation
No external libraries needed

🎓 Learning Outcomes

Master object creation and management

Understand access control and visibility

Practice inheritance, polymorphism, and method overriding

Explore abstract classes, design patterns, and advanced OOP concepts like association and composition

Apply decorators and custom object behaviors

Build real-world inspired class structures (e.g., calculators, binary trees, teams)

Practice these assignments to strengthen your Python OOP skills and prepare for real-world programming challenges! 🚀
