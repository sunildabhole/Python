class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"This number square is:{self.n*self.n}")

    def cube(self):
        print(f"This number square is:{self.n*self.n*self.n}")

    def square_root(self):
        print(f"This number square is:{self.n**1/2}")


c = Calculator(4)
c.square()
c.cube()
c.square_root()