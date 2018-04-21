class Bank:
    
    def __init__(self, balance):
        self.balance = balance

    def deposit(self,val):
        self.balance = self.balance + val

    def withdraw(self,val):
        self.balance = self.balance - val

class Rural(Bank):
    def __init__(self,bal):
        super().__init__(bal)
    def withdraw(self,bal):
        if(self.balance <= bal):
            print("Money not enought to withdraw!")
        else:
            super().withdraw(bal)


r1 = Rural(500)
r1.withdraw(20)
print(r1.balance)
