# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. 
# Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car "has-a" Engine

    def start_car(self):
        print("Starting the car...")
        self.engine.start()  # Using Engine's method

# Example usage
my_engine = Engine()
my_car = Car(my_engine)
my_car.start_car()