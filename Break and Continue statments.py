'''
A while loop in Python is used to execute a block of code repeatedly as long as a specified condition is True.

count = 1
while count <= 5:
    print("Count is:", count)
    count += 1  # Increment count
'''

i = 0
while(i<=5):
  print(i)
  i = i+1
'''
output
0
1
2
3
4
5
'''

userinput = int(input("Please enter a number"))
i=0
while(i<userinput):
  print(i)
  i=i+1
  
''' 
The break statement in Python is used to exit a loop prematurely when a certain condition is met. It immediately stops the loop execution and moves to the next statement outside the loop.
'''

i = 0
for i in range(10):
  print( "5 x ",i+1, "=", 5*(1+i))
  if(i==9):
    break




''' 
The continue statement in Python skips the current iteration of a loop and moves to the next iteration, without exiting the loop.

'''
i = 0

for i in range(20):
  if(i == 10): 
    print("You lost 10")
    continue
  print(i)
    
    
