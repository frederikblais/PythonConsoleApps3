#   
import cmath
import math

line = '------------------------------------------'
title = '|          Quadratic Calcuator           |'

# Header
print (line)
print (title)
print (line)

# Ask for input of int n
a = float(input('Enter the value for a: '))
b = float(input('Enter the value for b: '))
c = float(input('Enter the value for c: '))

print()

# solve the equation
def solve_quadratic(a,b,c):

    # calculating discriminant using formula 
    dis = b * b - 4 * a * c  
    sqrt_val = math.sqrt(abs(dis))  
      
    # checking condition for discriminant 
    if dis > 0:   
        trinomial = ((-b + sqrt_val)/(2 * a), (-b - sqrt_val)/(2 * a))
        print(trinomial)
      
    elif dis == 0:  
        trinomial = -b / (2 * a)
        print(trinomial)  
      
    # when discriminant is less than 0 
    else: 
        trinomial = ((- b / (2 * a), " + i", sqrt_val) , (- b / (2 * a), " - i", sqrt_val))
        print(trinomial) 
        
# solve the equation using complex numbers
def solve_quadratic_complex(a,b,c):
    d = (b**2) - (4*a*c)
    x = (-b-cmath.sqrt(d))/(2*a) # Calculating the first solution 
    z = (-b+cmath.sqrt(d))/(2*a)
    print(x,z)

# If a is 0, then incorrect equation 
if a == 0:  
        print("Input correct quadratic equation")  
  
else: 
    solve_quadratic(a,b,c)
    print()
    solve_quadratic_complex(a,b,c)