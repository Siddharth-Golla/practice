"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
"""

def uniques(duplicates:list) -> list:
    result = []
    for element in duplicates:
        if element not in result:
            result.append(element)
    return result



if __name__ == '__main__':
    list1 = [2,5,7,3,8,4,4,2,2,77,2,43,1,8,3,0]
    list2 = [x for x in "mississippi"]

    print(uniques(list1))
    print(uniques(list2))