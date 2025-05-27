# Create a class Logger that prints a message when an object is created (constructor)
#  and another message when it is destroyed (destructor).
# destructor only run in delete and end of the program

class Logger():
    def __init__(self):
        print("Message After: logger object is created") # constructor

    def __del__(self):
        print("Message Before: logger object is destroyed") # destructor

log = Logger()
del log