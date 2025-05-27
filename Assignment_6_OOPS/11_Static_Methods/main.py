# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) 
# that returns the Fahrenheit value.

class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# temp_c = 25
   
temp_f = TemperatureConverter.celsius_to_fahrenheit(25)
print(f"Fahrenheit value is: {temp_f}°F")
#print(f"{temp_c}°C = {temp_f}°F")

