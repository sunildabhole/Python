from random import randint

class Train:
    def __init__(self,trainno):
        self.trainNo = trainno

    def book(self,fro,to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no is: {self.trainNo}")

    def getFare(self,fro,to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(123454)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur","Delhi")