# i goes to 0 til n
# ex: n = 3
# e = 1/0! + 1/1! + 1/2! + 1/3!
# print (e)
import math

line = '------------------------------------------'
title = '|         FACTORIAL CALCULATOR           |'

# Header
print (line)
print (title)
print (line)

# Ask for input of int n
n = int(input('Enter the value for n: '))
print()

def value_e(n):
    return sum(1 / float(math.factorial(i)) for i in range(n))
 
print("The approximation of e is", 
value_e(n)) 