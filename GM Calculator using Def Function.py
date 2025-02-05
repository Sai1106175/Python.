'''
Definition of a Function
A function in Python is a reusable block of code that performs a specific task. It helps in code organization, reusability, and modular programming.

Types of Functions in Python
Built-in Functions – Predefined functions in Python, e.g., print(), len(), sum(), max(), min(), etc.
User-defined Functions – Functions created by the user to perform specific tasks.
Lambda Functions – Anonymous functions that can have only one expression.
Recursive Functions – Functions that call themselves for repetitive tasks.

'''



def calGM (a,b):
  GrossMargin = (a-b)/a
  GrossMargin = GrossMargin*100

  print("Your Gross Margin for the role is = ",GrossMargin)


a = int(input("Please enter your Bill Rate  "))
b = int(input("Please enter your cost Rate  "))
calGM(a,b)

