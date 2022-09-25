"""
Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument.
"""

def factorial(number:int) -> int:
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)


if __name__ == '__main__':
    number = 10
    print(f"The factorial of the number {number} is {factorial(number)}")