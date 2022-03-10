'''
BANK ACCOUNT CLASS
'''
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
###############################
'''
USER CLASS
'''
class User: 
    def __init__(self,name,checking_account,savings_account): #constructor function
        self.name = name
        self.balance = 1000
        self.checking_account = checking_account
        self.savings_account = savings_account
    def make_desposit(self, amount): 
        self.account.deposit(amount)
        return self
    def make_withdrawal(self,amount): #withdrawal function
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):  #function: display balance
        print(f"The Total Balance is:$ {self.checking_account.balance + self.savings_account.balance:,.2f}")
        print(f"Checking Account:$ {self.checking_account.balance:,.2f}")
        print(f"Saving Account:${self.savings_account.balance:,.2f}")
        return self
    def display_user_name(self): #function display user name
        print(self.name)
        return self

bank1 = BankAccount(.4, 5000)
bank2 = BankAccount(.7, 1000000)
x = User("Mustafa",bank1,bank2)
x.display_user_balance()