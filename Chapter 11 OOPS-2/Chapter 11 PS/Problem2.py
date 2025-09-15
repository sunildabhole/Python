class Animals:
    print("This class is Animal")

class Pet(Animals):
    print("This is pet animal")

class Dog(Pet):
    print("Dog class")

    @staticmethod
    def bark():
        print("Dog is bark method")

a = Animals()

b = Pet()

c = Dog()
c.bark()