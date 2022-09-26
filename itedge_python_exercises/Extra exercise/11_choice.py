from random import randrange
"""
6) Write a Python program to randomly select an item from a list.
"""

def choice_(data: list):
    """Implementation of function choice using randrange function

    Args:
        data (Sequence): Non empty list
    Returns:
        [type]: Random element from the list
    """
    return data[randrange(len(data))]


if __name__ == '__main__':
    print(choice_([1,2,3,4,5,6,7,9]))