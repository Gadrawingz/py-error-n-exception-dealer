# Declaring some variables
number = 20
not_a_number = "Any string"

# Try it
try:
   result = number + not_a_number
   print(result)

# TypeError: This exception is raised when an operation is applied
# to an object of the wrong type like adding int with string type
except TypeError:
    print("Custom Error: Cannot perform addition on int and string")

# Happy coding @gadiradufasha
