class Employee:
    language = "py" # This is the class attriutes
    salary = 1200000

    @staticmethod # It work like normal function inside the class
    def getinfo():
        print(f"This person name is {harry.name}, salary is {harry.salary}, and language is {harry.language}")

harry = Employee()
harry.name = "Harry"
print(harry.language,harry.salary)
harry.getinfo()   # called by method