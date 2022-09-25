"""
Write a Python function to check whether a number is in a given range.
"""

def in_range(number:int, lower:int, upper:int) -> bool:
    return number in range(lower, upper + 1)


print(in_range(5,1,10))