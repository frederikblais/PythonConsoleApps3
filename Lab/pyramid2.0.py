#
#   Prints a pyramid with custom characters
#


line = '------------------------------------------'
title = '|            PYRAMID 2.0                 |'

# Header
print (line)
print (title)
print (line)

# Ask for input of int n
n = int(input('Enter the value for n: '))
c = str(input('Enter a symbol: '))
print()

if(c == ''):
    c = '*'

def pyramid (*args):
    for i in range(n):
        for s in range(-n+1, -i):
            print(" ", end="")
        for j in range(i+1):
            print(c,"", end="")
        print()

pyramid(n,c)
print()
print (line)