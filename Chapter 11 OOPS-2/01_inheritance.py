class Employee:
    comapany = "ITC"

    def show(self,name,salary):
        self.name = name
        self.salary = salary
        print(f"The name of the company is {self.name} and the salary is {self.salary}")

class Programer(Employee):
    comapany = "IT"
    
    def showLanguage(self,name,language):
        self.name = name
        self.language = language
        print(f"The name is {self.name} and he is good with {self.language} language")


b = Programer()
b.show("L&T","30000")
b.showLanguage("Sunil","Python")