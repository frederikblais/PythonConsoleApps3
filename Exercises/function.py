# A function can be modified

def function():
    print("test")
function()

def function():
    print("test1")
function()

def function():
    print("test2")
function()

# This function is bad as its doing many things at once

value = int(input("Enter a value: "))
value2 = int(input("Enter a value: "))

def addtwo(a,b):
    result = a+b
    return result

total = addtwo(value,value2)
print("The new value is: ",total)