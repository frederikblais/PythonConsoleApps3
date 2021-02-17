# (*args) lets the parameter passed to be a list

def perimeter (*args):
    sides = len (args)
    print ("There are: ",sides, "side to the object.")
    total = 0
    for i in range (0,sides):
        total = total + args[1]
    return total

triangle = perimeter (4,6,10)
print ("The perimeter is: ", triangle)

rectangle = perimeter (4,8,4,8)
print ("The perimeter is: ", rectangle)