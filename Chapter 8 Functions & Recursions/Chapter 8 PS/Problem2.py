# Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
fahrenheit = int(input("Enter temperature in Fahrenheit: "))
print("Fahrenheit to Celsius:", round(fahrenheit_to_celsius(fahrenheit), 2), "°C")



# Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = int(input("Enter temperature in Celsius: "))
print("Celsius to Fahrenheit:", round(celsius_to_fahrenheit(celsius), 2), "°F")

