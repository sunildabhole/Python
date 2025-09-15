class Programer1:
    company = "IT"
    def showLanguage(self):
        self.name = "Sunil"
        self.language = "Python"
        print(f"The name is {self.name} and he is good with {self.language} language")

class Programer2:
    company = "Cyber Security"
    def showLanguage1(self):
        self.name = "Prabhu"
        self.language = "Java"
        print(f"The name is {self.name} and he is good with {self.language} language")

class Employee(Programer1, Programer2):
    company = "ITC"
    def show(self):
        self.name = "L&T"
        self.salary = 30000
        print(f"The name of the company is {self.name} and the salary is {self.salary}")


b = Employee()
b.show()
b.showLanguage()
b.showLanguage1()