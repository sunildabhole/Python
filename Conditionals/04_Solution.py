fruit = input("Enter fruit name: ")
color = input("Enter fruit color to check ripeness(Green,Yellow,Brown): ")

if fruit == "Banana":
    if color =="Green":
        print("This is Unripe")
    elif color == "Yellow":
        print("This fruit is Ripe")
    elif color == "Brown":
        print("This fruit is OverRipe")
else:
    print(fruit," Fruit information not available")