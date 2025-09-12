class Employee:
    language = "py" # This is the class attriutes
    salary = 1200000

harry = Employee()
harry.name = "Harry" # This is the object attributes
print(harry.name,harry.language,harry.salary)

ram = Employee()
ram.name = "Ram"
print(ram.name,ram.language,ram.salary)

# Here name is object Attribute and salary & name is class Attributes as they directly belongs to the class