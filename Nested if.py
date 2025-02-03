userenternumber = int(input("Please enter the number"))

if(userenternumber<0):
  print("The entered number is negative.")
elif(userenternumber>0):
  if(userenternumber<= 10):
    print("User entered number is inbetween 0-10 ")
  elif(userenternumber>=11 and userenternumber<20):
    print("user entered number is inbetween 10-20")
  elif(userenternumber>=21 and userenternumber<30):
    print("User entered number is in between 20-30")
  else:
    print("user entered number is more then 30")

else:
  print("use entered number is zero")
  
