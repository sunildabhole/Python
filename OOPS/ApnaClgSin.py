class Car:
    def __init__(self):
        print("Single level Inheritance")

    def start(self):
        print("Car is Startet")

class ToyotaCar(Car):
    def __init__(self,color):
        super().__init__()
        self.color = color

c = ToyotaCar("Yellow")
c.start()
print(c.color)