class Car:
    def __init__(self, brand, model):
        self.__brand = brand     # Private attribute
        self.model = model

    def get_brand(self):           # Getter method (not using @property yet)
        return self.__brand + " !!"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Disel & Petrol"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla","Mosel S","85kHw")
# print(my_tesla.__brand)
print(my_tesla.fuel_type())

safari = Car("Tesla" , "Korola")
print(safari.fuel_type())