userenteredtime = float (input("Please enter the time in 24 hours format."))

if(userenteredtime >= 0.00 and userenteredtime <= 24.00):
  print("Checking the Time.......")
  if(userenteredtime >=0.00 and userenteredtime <= 11.59):
    print("Now the time",userenteredtime, "Good Morining")
  elif(userenteredtime >= 12.01 and userenteredtime <= 16.00):
    print("Now the time",userenteredtime, "Good Afternoon")
  else:
    print("Now the time",userenteredtime, "Good evening")

else:
  print("Please enter the correct time.")

print("Thankyou for using it.")
   
  
  
