"""Ask the user to input two numbers, divide them and print the result.

What is the result type? Print it out.
"""
numerator = input("Enter first number(any): ")
denominator = input("Enter second number(other than 0): ")
result = int(numerator) / int(denominator)
print(f"{numerator} / {denominator} = {result}")
print(f"The type of result is {type(result)}")