# The recursion will loop until you reach the condition num = 0
def factorial (num):
    if (num == 0):
        return 1
    else:
        return num * factorial (num - 1)

result = factorial(5)
print ("The factorial of 5 is: ", result)