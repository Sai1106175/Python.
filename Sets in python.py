
"""
Sets in python.

A set in Python is an unordered collection of unique elements. It is defined using curly braces {} or the built-in set() function. Sets are useful when you need to store distinct values and perform mathematical set operations like union, intersection, and difference.

"""

a  = {1,2,3,4,5,6,77,5,100}
b  ={2,34,4,5,6,5,5,2000}

c=a.union(b) # Union means combining the two sets and presenting the values which are not repetative.

print(c)


c  = {1,2,3,4,5,6,77,5,100}
d  ={2,34,4,5,6,5,5,2000}

e=c.intersection(d) # Prints the value which are very common in both the sets.

print(e)


fieee = {"Sharan", "Varun", "jyothi"}
a2 = {"karthik", "SSS", "pratdeeet"}

print(fieee.isdisjoint(a2))# which finds the value of both the values are not same it returs ture value.

#Superset.

fieee = {"Sharan", "Varun", "jyothi"}
a2 = {"karthik", "SSS", "pratdeeet"}
a3 = {"Sharan","Varun"}

print(fieee.issuperset(a2))
print(fieee.issuperset(a3))

#update
fieee = {"Sharan", "Varun", "jyothi"}
a2 = {"karthik", "SSS", "pratdeeet"}
a3 = {"Sharan","Varun"}

fieee.add("Kk")

print(fieee)



# Adding an element
my_set.add(6)

# Adding multiple elements
my_set.update([7, 8, 9])

# Removing an element (throws KeyError if not found)
my_set.remove(3)

# Removing an element (avoids error if element not found)
my_set.discard(10)

# Removing and returning an arbitrary element
popped_element = my_set.pop()

# Clearing all elements
my_set.clear()
