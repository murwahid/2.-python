'''
Basic - Print all integers from 0 to 150.
Multiples of Five - Print all the multiples of 5 from 5 to 1,000
Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
'''
# """ Print all numbers 0-150"""
def all_numbers():
    for x in range(0,151):
        print(x)

all_numbers()

#multiples of 5 
def five_multiples(): 
    for x in range(5,1001):
        if x %5==0: 
            print(x)       

#function call 
five_multiples()

# Counting, the Dojo Way 
def dojo_way(): 
    for x in range(1,101):
        if x %5==0: 
            print("Coding")
        elif x%10==0:
            print("Coding Dojo")
        else: 
            print(x)
dojo_way()

#Whoa. That Sucker's Huge add odd integers from 0 to 500,000
def huge_add(): 
    numbers = []
    for x in range(0,500000):
        if x%2==1:
            numbers.append(x)
    big_output = sum(numbers)
    print(big_output)

# huge_add()

#Countdown by Fours: Print positive numbers starting at 2018, counting down by fours.

def count_fours(): 
    for x in range(2018,0,-4):
        print(x)

count_fours()

#Flexible Counter - Set three variables: lowNum, highNum, mult.

lowNum=2
highNum=9
mult=3

for x in range(lowNum,highNum+1): 
    if x%mult == 0:
        print(x)
