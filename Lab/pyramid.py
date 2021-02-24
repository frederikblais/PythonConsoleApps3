
line = '------------------------------------------'
title = '|         PYRAMID CALCULATOR             |'

# Header
print (line)
print (title)
print (line)

# Ask for input of int n
n = int(input('Enter the value for n: '))
print()

def pyramid (n):
    print()
    for i in range(n):
        for s in range(-n+1, -i):
            print(" ", end="")
        for j in range(i+1):
            print("* ", end="")
        print()

pyramid(n)
print (line)