"""
A dictionary in Python is an unordered, mutable collection of key-value pairs. It is defined using curly braces {} or the built-in dict() function.

"""


classData = {"Name":"Sharan", "Rol Number": 56, "Age":27}
print(classData["Name"])

print(classData.get('Age')) 

print(classData.keys()) # Which prints the Keys of the dictonary

print(classData.values()) # Which Prints the values of the dictonary

print(classData.items())

for Keys,values in classData.items():
    print(f"{Keys}  the value assigned is {values}")

#Methods.


Class2 ={101:44,102:55,103:99,104:88,105:78}
Class2a={109:88,108:33,107:66,106:33}
Class2.update(Class2a) # Update one dic with another.
print(Class2)

for key,values in Class2.items():
    if(values>=90):
        print(f"{key} would fall under A cader as he secured {values}")


Class2 ={101:44,102:55,103:99,104:88,105:78}
Class2a={109:88,108:33,107:66,106:33}
Class2.update(Class2a)
print(Class2)

del Class2[101] # Delete the particular mentioned key from the dictorary
del Class2 # Delete the complete list of dictoonary

print(Class2)

"""

dict.keys()	Returns all keys.
dict.values()	Returns all values.
dict.items()	Returns all key-value pairs as tuples.
dict.get(key, default)	Returns value for key, or default if key not found.
dict.update(dict2)	Updates the dictionary with key-value pairs from dict2.
dict.pop(key, default)	Removes key and returns value, or default if key not found.
dict.popitem()	Removes and returns the last inserted key-value pair.
del dict[key]	Deletes the key from the dictionary.
dict.clear()	Removes all items.
key in dict	Checks if a key exists.
dict.copy()	Returns a shallow copy.
dict.fromkeys(iterable, value)	Creates a dictionary with keys from iterable.
dict.setdefault(key, default)	Returns value if key exists, else sets default.
"""
