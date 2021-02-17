number = 1

while number <=5:
    print(number)
    number += 1

    #use break to exit the while and skip else
    if(number == 5):
        break
    
else:
    print('Done ...')