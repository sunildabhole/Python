class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum = sum + i
        sum = sum /3
        print("Student name is: ",s.name," & Marks avarage is: ",round(sum,2))


s = Student("Sunil",[90,80,60])
s.get_avg()