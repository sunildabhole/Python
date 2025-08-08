distance = int(input("Please enter transportation distance: " ))

if distance < 3:
    mode = "Walk"
elif distance <= 15:
    mode = "Bike"
else:
    mode = "Car"

print("This is mode use you ->",mode)