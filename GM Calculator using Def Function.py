def calGM (a,b):
  GrossMargin = (a-b)/a
  GrossMargin = GrossMargin*100

  print("Your Gross Margin for the role is = ",GrossMargin)


a = int(input("Please enter your Bill Rate  "))
b = int(input("Please enter your cost Rate  "))
calGM(a,b)

