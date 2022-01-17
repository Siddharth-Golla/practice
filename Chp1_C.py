from typing import Sequence

# C-14) Write a short Python function that takes a sequence of integer values and
#   determines if there is a distinct pair of numbers in the sequence whose
#   product is odd.


def is_odd_product(data: Sequence) -> bool:
    """Returns True if distinct pair of numbers whose product is odd is found in the sequence
        else return False

    Args:
        data (Sequence): List of positive integer values

    Returns:
        bool: True if product of two values is odd else False
    """
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] != data[j] and (data[i] * data[j]) % 2 == 1:
                return True
    else:
        return False


print(is_odd_product([2, 4, 6, 9, 11]))


# C-15) Write a Python function that takes a sequence of numbers and determines
#   if all the numbers are different from each other (that is, they are distinct).

def is_distinct(data) -> bool:
    """Returns True if all the numbers in sequence are different from each other
        else return False

    Args:
        data (Sequence): List of positive integer values

    Returns:
        bool: False is any two values are same else True
    """
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                return False
    else:
        return True

# C-18) Demonstrate how to use Python’s list comprehension syntax to produce
#   the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
