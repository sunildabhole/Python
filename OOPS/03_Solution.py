class Car:
    def __init__(self,model,color):
        self.model = model
        self.color = color

    def full_name(self):
        return f"{self.model}:{self.color}"
    
class Battery(Car):
    def __init__(self,model,color,battery_size):
        super().__init__(model,color)
        self.battery_size = battery_size

new = Battery("xyx","red","60kWh")

print("Name: ",new.model)
print("Color: ",new.color)
print("Full Name: ",new.full_name())
print("Size Of Battery: ",new.battery_size)