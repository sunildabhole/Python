class Employee:
    a = 1

    @classmethod
    def show(self):
        print(f"The class attributes of a is {self.a}")

e = Employee()
e.show()