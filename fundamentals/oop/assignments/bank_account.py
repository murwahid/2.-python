class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        #increment balance
        self.balance +=amount
        return self
    def withdraw(self, amount):
        #decrement balance
        self.balance -=amount
        return self
    def display_account_info(self):
        print(f"The balance is :$ {self.balance}")
        print(f"The interest rate is: {self.int_rate}")
    def yield_interest(self): 
        if self.balance > 0:
            yld = self.balance * self.int_rate
            print(f"Interest Yield is: {yld}")
        else:
            print('Balance is negative. No Yield.')
        return self

# account 1
x = BankAccount(4,5000)
x.deposit(5000).deposit(5000).deposit(5000).withdraw(100).display_account_info()

#account 2
y = BankAccount(7,10000)
y.deposit(25000).deposit(9000).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()