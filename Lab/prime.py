
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
        # prime numbers are greater than 1
    if n > 1:
    # check for factors
        for i in range(2,n):
            if (n % i) == 0:
                state = False
                print(state)
                print()
                break
            else:
                state = True
                print(state)
                print()
        
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(n,"is not a prime number")

def output():

    for i in range (2,100,1):
        num = 2;
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num, ' is not prime')
                num +=1
                break
            else:
                print(num, ' is prime')
                num += 1

if(n > 2):
    is_prime(n)
    output()


else:
    print('You must enter a value greater than 2.')