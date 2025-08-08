import math

def circle(radius):
    area = math.pi * (radius ** 2)

    circumference = 2 * math.pi * radius

    return(round(area, 2),round(circumference, 2))

a, c = circle(3)

print("Area: ",a," Circumference: ",c)