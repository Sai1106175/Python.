Functions in Python

'''
Function Arguments.

Default Arguments - A default argument in Python is a function parameter that has a default value assigned to it. If the caller does not provide a value for that parameter, the default value is used.

'''

def message(name,message = "Good Morning"):
  print(message, name)

message("sai", "Fuckyou")

'''
output 

Fuckyou Sai.
'''


def message(name,message = "Good Morning"):
  print(message, name)

message("sai")

'''
Output 

Good Morning Sai
'''
'''
Required arguments are function parameters that must be provided when calling the function. If a required argument is missing, Python raises a TypeError.



Keyword Arguments
Keyword arguments (also known as named arguments) are a way to pass arguments to a function using the parameter name as a reference. This allows arguments to be specified out of order and improves code readability.

'''
