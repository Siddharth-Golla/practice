from random import randrange
from typing import Sequence

# R-1.1) Write a short Python function, is_multiple(n, m), that takes two integer values and
# returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise


def is_multiple(n: int, m: int) -> bool:
    """Takes two values n and m to check if n is multiple of m.

    Args:
        n (int): The greater value to be checked
        m (int): The smaller factor

    Returns:
        bool: Returns True if m is factor of n else False
    """
    if n % m == 0:
        return True
    else:
        return False


# R-1.2) Write a short Python function, is_even(k), that takes an integer value and
#   returns True if k is even, and False otherwise. However, your function
#   cannot use the multiplication, modulo, or division operators

def is_even(k: int) -> bool:
    is_even = True
    for _ in range(1, k+1):
        if is_even is True:
            is_even = False
        else:
            is_even = True

    return is_even


# R-1.3) Write a short Python function, minmax(data), that takes a sequence of one or more numbers,
# and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use
# the built-in functions min or max in implementing your solution.

def minmax(data):
    smallest = data[0]
    largest = data[-1]
    for number in data:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number
    return (smallest, largest)


# R-1.4) Write a short Python function that takes a positive integer n and
#   returns the sum of the squares of all the positive integers smaller than n.
# R-1.5) Give a single command that computes the sum from Exercise R-1.4,
#   relying on Python’s comprehension syntax and the built-in sum function.

def sum_of_squares1(n: int) -> int:
    assert n >= 1, "n should be a positive integer."
    total = 0
    for i in range(1, n):
        total = total + i**2
    return total


def sum_of_squares2(n: int) -> int:
    assert n >= 1, "n should be a positive integer."
    return sum([i**2 for i in range(1, n)])


# R-1.6) Write a short Python function that takes a positive integer n
#   and returns the sum of the squares of all the odd positive integers smaller than n.
# R-1.7) Give a single command that computes the sum from Exercise R-1.6,
#   relying on Python’s comprehension syntax and the built-in sum function.

def sum_of_oddsquares1(n: int) -> int:
    assert n >= 1, "n should be a positive integer."
    total = 0
    for i in range(1, n):
        if i % 2 == 1:
            total = total + i**2
    return total


def sum_of_oddsquares2(n: int) -> int:
    assert n >= 1, "n should be a positive integer."
    return sum([i**2 for i in range(1, n) if i % 2 == 1])


# R-1.8) What parameters should be sent to the range constructor,
# to produce a range with values 50, 60, 70, 80?

list1 = list(range(50, 81, 10))

# R-1.9) What parameters should be sent to the range constructor,
# to produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

list2 = list(range(8, -9, -2))

# R-1.10) Demonstrate how to use Python’s list comprehension syntax
# to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

list3 = [2**i for i in range(0, 9)]


# R-1.11)  Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes a more basic
# function randrange, with parameterization similar to the built-in range function,
# that return a random choice from the given range. Using only the randrange function,
# implement your own version of the choice function.


def choice_(data: Sequence):
    """Implementation of function choice using randrange function

    Args:
        data (Sequence): Any non-empty sequence

    Returns:
        [type]: Random element from the sequence
    """
    return data[randrange(len(data))]


if __name__ == "__main__":

    print(list1)
    print(list2)
    print(list3)
    print(choice_([2, 3, 5, 7, 9, 3]))
