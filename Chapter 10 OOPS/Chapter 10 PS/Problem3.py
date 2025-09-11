class Demo:
    a = 3

d = Demo()
print(d.a) # Print the class attribute because instance attribute is not present.
d.a = 0 # Intance attribute is present.
print(d.a) # Print the intance attribute because intance attribute is present.
print(Demo.a) # PRints the class attribute