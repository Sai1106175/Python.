DocString and Pep -8 

A docstring (short for documentation string) is a multi-line string used to document a module, function, class, or method in Python. It provides an explanation of the purpose, usage, and behavior of the code.

A docstring is written using triple double-quotes (""" """) or triple single-quotes (''' ''') immediately after the definition of a function, class, or module.


def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.
    
    Parameters:
    a (int, float): The first number
    b (int, float): The second number
    
    Returns:
    int, float: The sum of the input numbers
    """
    return a + b
