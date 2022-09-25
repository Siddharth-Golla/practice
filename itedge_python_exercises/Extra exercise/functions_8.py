"""
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
"""



def case_sum(string: str) -> tuple:
    """Calculates the number of upper case letters and lower case letters in string

    Args:
        string (str): The string whose number of upper case and lower case is to be calculated

    Returns:
        tuple: Contains number of upper case letters and number of lower case letters
    """    
    upper_counter = 0
    lower_counter = 0
    for alphabet in string:
        if alphabet == """ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""":
            continue
        if alphabet.isupper():
            upper_counter += 1
        if alphabet.islower():
            lower_counter += 1
    
    return (upper_counter, lower_counter)

if __name__ == '__main__':
    string = "Hello Bob, How are you?"
    print(case_sum(string))