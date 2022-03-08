#1:[x]
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# Prediction: 5

#2:[x]
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Prediction: error


#3:[x]
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

# Prediction:5


#4[x]
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# Prediction: 5

#5:[x]
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# Prediction: 5

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# Prediction: 8

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# Prediction:"2 5"

#8 [x]
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# Prediction: 100, 10

#9[x]
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Prediction:7
# Prediction:14
# Prediction: 7 + 14 = 21

#10 [x]
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Prediction:8

#11 [x]
b = 500
print(b)# Prediction:500
def foobar():
    b = 300
    print(b)
print(b)# Prediction:500
foobar()# Prediction:300
print(b)# Prediction:500


#12
b = 500
print(b) # Prediction:500
def foobar():
    b = 300
    print(b)
    return b
print(b) # Prediction:500
foobar() # Prediction:300
print(b) # Prediction:500


#13
b = 500
print(b) #Prediction:500
def foobar():
    b = 300
    print(b)
    return b
print(b) #Prediction:500
b=foobar() #Prediction:300
print(b)#Prediction:300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# Prediction: 1 3 2

#15
def foo():
    print(1) #1
    x = bar() #3, returns 5 x=5
    print(x) #5
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# Prediction: 1,3,5
# Prediction: 10