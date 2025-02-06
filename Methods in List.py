i = [13,35,67,88,6,5545,454]

# i.reverse()
# print(i)

# i.append(1) # Add the values to the list.
# print(i)

# i.sort() # revevers the given string.
# print(i)


# i.sort(reverse=True) # rerevevers the given string.
# print(i)

s=i # when you are creating the replica of list of items and assigning it to different variable directly and changing the idex values in duplicate variable., it effeccts to the orginal list tooo.
s[0]= 0
print(s) 
print(i)

"""
in order to create the rightway of copying of list..
"""

j=i.copy()
j[1] = 0
print(j) 
print(i) # The list of i wont effect with the changes of duplicate list..

i.insert(1,99) #insert function used to replace the value with the given index and after the value to be inserted.
print(i) 

m = [1222,23232,43435,34355]
i.extend(m) # When we are trying to add the list with one list with anther list. we use extend method.
print(i)

