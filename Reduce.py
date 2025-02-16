from functools import reduce

numbers = [2,3,4,5,5,5,6]

def decreasevalue (x,y):
    return (x+y)
    
newlist = reduce(decreasevalue,numbers)

print(newlist)
