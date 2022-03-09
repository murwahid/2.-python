class User: 
    def __init__(self,name): #constructor function
        self.name = name
        self.balance = 1000
    def make_desposit(self, amount): 
        self.balance += amount
        return self
    def make_withdrawal(self,amount): #withdrawal function
        self.balance -= amount
        return self
    def display_user_balance(self):  #function: display balance
        print("The Balance is: $ " + str(self.balance))
        return self
    def display_user_name(self): #function display user name
        print(self.name)
        return self
    def transfer_money(self, other_user, amount): 
        self.balance -= amount
        other_user.balance += amount
        print(f"{self.name} makes a transfer of {amount} to {other_user.name}")
        return self

# #user 1
x = User("Mindy") #create user

x.display_user_name() #display name
x.make_desposit(1000).make_desposit(1000).make_desposit(1000).make_withdrawal(100) .display_user_balance() #function: Display Balance

#user 2
y = User("Rick")
y.display_user_name().make_desposit(500).make_desposit(500).make_withdrawal(10000).make_withdrawal(1000).display_user_balance()

#user 3 1 d, 3w
z = User("Jeff").display_user_name().make_desposit(500000).make_withdrawal(1000).make_withdrawal(1000).make_withdrawal(1000).display_user_balance()
z.transfer_money(y,50000)



