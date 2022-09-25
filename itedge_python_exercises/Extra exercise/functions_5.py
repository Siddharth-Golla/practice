"""
Write a Python function to sum all the numbers in a list. Sample List : (8, 2, 3, 0, 7)
"""

def list_sum(numbers:list) -> int:
    total = 0
    for number in numbers:
        total = total + number
    return total


if __name__ == '__main__':
    print(list_sum([8,2,3,0,7]))
    print(list_sum([1,2,3,4,5,6,7,8,9,10]))