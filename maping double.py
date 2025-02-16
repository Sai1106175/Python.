def doubling (x):
    return (x+x)


number = [1,3,3,4,5,6,7,6,5]

newlist = list(map(doubling,number))

print(newlist)
