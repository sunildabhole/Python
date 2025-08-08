class Sunil:
    def __init__(self,address,city,marks):
        print("My name is: Sunil Samadhan Dabhole")
        self.address = address
        self.city = city
        self.marks = marks
    def welcome(self):
        print("Welcome Student",self.city)
    
    def tmarks(self):
        return self.marks
s = Sunil("A/P-Waghapur","Kolhapur",95)

# print(s.address,":",s.city)

# s2 = Sunil("Malawadi","Jaypur")
# print(s2.address,":", s2.city)
s.welcome()
print(s.tmarks())