# Print inches to centimeters
def inch_to_cm(n):
    if n == 0:
        return
    return n * 2.54

n = int(input("Enter a number in inches: "))
result = inch_to_cm(n)
print(f"{n} inches is equal to {result} centimeters") if result else print("Please enter a positive number.")