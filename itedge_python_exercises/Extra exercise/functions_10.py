"""
Write a Python function to return a list of even numbers from a given list.
"""

def evens(numbers:list) -> list:
    """Returns a list of even numbers from a list of numbers

    Args:
        numbers (list): List of number from which even numbers is to be selected.

    Returns:
        list: A list of even numbers
    """    
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    
    return result

if __name__=='__main__':
    list1 = [3,6,4,8,3,1,10,11,17]
    list2 = [0,2,4,6,8,10,12]
    list3 = [1,3,5,7,9,11]
    print(evens(list1))
    print(evens(list2))
    print(evens(list3))