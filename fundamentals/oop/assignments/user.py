class User: 
    def __init__(self,name): #constructor function
        self.name = name
        self.balance = 1000
    def make_desposit(self, amount): 
        self.balance += amount
    def make_withdrawal(self,amount): #withdrawal function
        self.balance -= amount
    def display_user_balance(self):  #function: display balance
        print("The Balance is: $ " + str(self.balance))
    def display_user_name(self): #function display user name
        print(self.name)

#user 1
x = User("Mindy") #create user

x.display_user_name() #display name
x.make_desposit(1000)
x.make_desposit(1000)
x.make_desposit(1000)
x.make_withdrawal(100) #function: withdrawal
x.display_user_balance() #function: Display Balance

#user 2
y = User("Rick")
y.display_user_name()
y.make_desposit(500)
y.make_desposit(500)
y.make_withdrawal(10000)
y.make_withdrawal(1000)
y.display_user_balance()

#user 3 1 d, 3w
z = User("Jeff")
z.display_user_name()
z.make_desposit(500000)
z.make_withdrawal(1000)
z.make_withdrawal(1000)
z.make_withdrawal(1000)
z.display_user_balance()
