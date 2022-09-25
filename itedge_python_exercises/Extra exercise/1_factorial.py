"""
Program to find factorial of number provided by the user.
"""

number = int(input("Enter a positive integer to find its factorial: "))
fact = 1
for i in range(2, number + 1):
    fact = fact * i
print(f"The factorial of {number} is {fact}.")