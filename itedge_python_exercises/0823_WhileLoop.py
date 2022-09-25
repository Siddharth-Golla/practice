"""
Ask the user to input an integer.
Print out all the numbers that are divisible by 17, that are less than user's number.
"""

number = int(input("Enter a positive integer: "))
while number > 1:
    number = number - 1
    if number % 17 == 0:
        print(number)