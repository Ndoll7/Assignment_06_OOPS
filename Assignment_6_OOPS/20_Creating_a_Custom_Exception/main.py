# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. 
# Handle it with try...except.

# Define custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18"):
        super().__init__(message)

# Define function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be at least 18.")
    print("Age is valid.")

# Example usage with exception handling
try:
    check_age(17)
except InvalidAgeError as e:
    print("Caught an exception:", e)
