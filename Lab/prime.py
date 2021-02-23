
line = '------------------------------------------'
title = '|          PRIME CALCULATOR             |'

# Header
print (line)
print (title)
print (line)

# Ask for input of int n
n = int(input('Enter a integer greater than 2: '))
state = False
print()

def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2,n):
            if n % i == 0:
                status = False
    return status

if is_prime(n):
    if n==97:
        print(n, "is a prime number")
        print()
    else:
        print(n, "is a prime number")
        print()
else:
    print(n, "is not a prime")
    print()

for n in range(2,101):
    if is_prime(n):
        if n==97:
            print(n, "is a prime number")
        else:
            print(n, "is a prime number")
    else:
        print(n, "is not a prime")