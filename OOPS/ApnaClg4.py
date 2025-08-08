class Axix:
    def __init__(self,bal,acc_no):
        self.balance = bal
        self.account_no = acc_no

    def debit(self,amount):
        self.balance -= amount
        print(amount," is debit")
        print("rs",self.total_amount())

    def credit(self,amount):
        self.balance += amount
        print(amount," is credit")
        print("rs",self.total_amount())

    def total_amount(self):
        return self.balance



a = Axix(70000,654321)
print("Total Amount is: ",a.balance)
a.debit(10000)
a.credit(10000)