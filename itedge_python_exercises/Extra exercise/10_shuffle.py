from random import randint
"""
Write a Python program to shuffle the following elements randomly. Go to the editor

Sample elements : [1, 2, 3, 4, 5, 6, 7]

Expected Output :

[2, 1, 7, 5, 3, 4, 6]
"""

def shuffle_(data:list) -> list:
    """ Returns a shuffled list using randint.

    Args:
        data (list): A non-empty list

    Returns:
        list: List with elements randomly reordered.
    """
    last_index = len(data) - 1
    while last_index > 0:
        rand_index = randint(0, last_index)
        data[last_index], data[rand_index] = data[rand_index], data[last_index]
        last_index -= 1
    return data


if __name__ == '__main__':
    print(shuffle_([1, 2, 3, 4, 5, 6, 7]))