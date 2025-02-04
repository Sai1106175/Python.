#Match Case Statements.

#The match-case statement in Python is a control flow construct introduced in Python 3.10 that allows for structural pattern matching. It is similar to switch-case in other languages but more powerful, allowing pattern-based matching of data structures.
#Definition:
#A match-case statement in Python allows for matching a value or structure against multiple patterns, executing the corresponding block of code when a pattern matches.

userInput = int(input("Please enter then Number"))

match userInput:

  case 0:
    print("entered number is",userInput, "Zero")
  case 1:
    print("Entered Number is ",userInput, "One")
  case 2:
    print("Entered number is 2")
  case _:
    print("The enered number is not 0,1,2 as well.")

