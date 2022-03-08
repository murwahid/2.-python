num1 = 42 #variable declaration
num2 = 2.3 #log statement
boolean = True #type check
string = 'Hello World' #Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#Dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #initialize
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name']) #access value
person['name'] = 'George' #change value
person['eye_color'] = 'blue' #add value
print(fruit[2]) #delete value

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

#conditional
if len(string) < 5: #if
    print("It's a short word!") 
elif len(string) > 15: #else if
    print("It's a long word!")
else: #else
    print("Just right!")

#for loop
for x in range(5): #start
    print(x) #stop
for x in range(2,5): #increment
    print(x) #break
for x in range(2,10,3):
    print(x)
x = 0
#while loop
while(x < 5): #start
    print(x) #stop
    x += 1 

pizza_toppings.pop()
pizza_toppings.pop(1)

#function
print(person) #parameter
person.pop('eye_color') #argument
print(person) #return

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) #NameError: name <variable name> is not defined
# num3 = 72 #
# fruit[0] = 'cranberry'
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7]) #IndexError: list index out of range
#   print(boolean) #IndentationError: unexpected indent
# fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'