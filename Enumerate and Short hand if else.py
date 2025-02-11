

#Short Hand if else.

a = 10
b = 20
print ("A") if a<b else print ("=") if (a == b) else print ("B")


"""
The index() function in Python is used to find the first occurrence of a specified value in a list, tuple, or string. 
If the value is found, it returns the index of the first matching element; otherwise, it raises a ValueError.

The enumerate() function in Python adds a counter to an iterable and
 returns it as an enumerate object, which can be converted into a list, tuple, or directly used in loops.

"""


marks = [10,20,30,40,50,60,70]

index = 0
for mark in marks:
    print (mark)
    index = index + 1 
    if (index == 4):
        print ("Sai You are Awesome.")


marks = [10,20,30,40,50,60,70]

for index, mark in enumerate(marks):
    print (mark)
    if (index == 4):
        print ("Sai You are Awesome.")



#Enumerate and index
marks = ["Sai", "Sharan", "Varun", "Jyothi", 9]

for index, mark in enumerate(marks,start =3): # You can specify the index number from where it should start.
    print (mark)
    if (index == 4):
        print ("Sai You are Awesome.")
        continue 
