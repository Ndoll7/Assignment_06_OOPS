# Create a class MathUtils with a static method add(a, b) that returns the sum.
#  No class or instance variables should be used. 

class MathUtils():

    @staticmethod
    def add(a, b):
        return a + b
    
result = MathUtils.add(10 , 10)
print(f"Sum of 2 numbers are: {result}")

    

