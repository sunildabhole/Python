class Employee:
    name = "L&T"
    salary = 30000
    def show(self):
        print(f"The name of the company is {self.name} and the salary is {self.salary}")


class Programer1(Employee):
    name = "Sunil"
    language = "Python"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


class ProgramerManager(Programer1):
    name = "Prabhu"
    language = "Java"
    def showLanguage1(self):
        
        print(f"The name is {self.name} and he is good with {self.language} language")

p = Programer1()
p.show()
p.showLanguage()

b = ProgramerManager()
b.show()
b.showLanguage()
b.showLanguage1()