class Programmer:
    company = "Microsoft"

    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

s = Programmer("Sunil",40000,416209)
print(s.name,s.salary,s.pin,s.company)

p = Programmer("Prabhu",50000,416203)
print(s.name,s.salary,s.pin,s.company)