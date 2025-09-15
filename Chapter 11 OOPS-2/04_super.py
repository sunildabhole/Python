class Employee:

    def __init__(self):
        print("Constructor of Employee")

    def show(self):
        self.name = "L&T"
        self.salary = 30000
        print(f"The name of the company is {self.name} and the salary is {self.salary}")


class Programer1(Employee):

    def __init__(self):
        super().__init__()
        print("Constructor of Programer1")

    def showLanguage(self):
        self.name = "Sunil"
        self.language = "Python"
        print(f"The name is {self.name} and he is good with {self.language} language")


class ProgramerManager(Programer1):

    def __init__(self):
        print("Constructor of ProgramerManager")

    def showLanguage1(self):
        self.name = "Prabhu"
        self.language = "Java"
        print(f"The name is {self.name} and he is good with {self.language} language")

p = Programer1()
p.show()
p.showLanguage()

b = ProgramerManager()
b.show()
b.showLanguage()
b.showLanguage1()