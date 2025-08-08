class Account:
    def __init__(self,bal,acc_no):
        self.balance = bal
        self.account_no = acc_no

    def debit(self,amount):
        self.balance -= amount
        print("RS",amount,"was debited")
        print("Total balance: ",self.total_balance())

    def credit(self,ammount):
        self.balance += ammount
        print("rs",ammount,"was credited your account")
        print("Total balance: ",self.total_balance())

    def total_balance(self):
        return self.balance
    

acc1 = Account(50000,1223456)
acc1.debit(10000)
acc1.credit(20000)
