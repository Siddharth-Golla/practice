"""Ask the user to input a number of type float.
Multiply it by pi = 3.14159
Print the type of the resulting variable.
Print the result.
"""

number = input("Enter a floating point number: ")
pi = 3.14159
result = float(number) * pi
print(f"{number} * pi = {result}")
print(f"The type of result is {type(result)}")