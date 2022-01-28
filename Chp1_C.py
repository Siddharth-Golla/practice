from cmath import sqrt
from random import randint
from typing import Sequence
from array import array

# C-1.14) Write a short Python function that takes a sequence of integer values and
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


# C-1.15) Write a Python function that takes a sequence of numbers and determines
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


# C-1.18) Demonstrate how to use Python’s list comprehension syntax to produce
#   the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

list1 = [(x**2) + x for x in range(10)]
print(list1)


# C-1.19) Demonstrate how to use Python’s list comprehension syntax to produce
#   the list [ a , b , c , ..., z ], but without having to type all 26 such
#   characters literally.

alpha_list = [chr(x) for x in range(97, 123)]
print(alpha_list)


# C-1.20) Python’s random module includes a function shuffle(data) that accepts a
#   list of elements and randomly reorders the elements so that each possible order occurs with equal probability.
#   The random module includes a more basic function randint(a, b) that returns a uniformly random integer
#   from a to b (including both endpoints). Using only the randint function,
#   implement your own version of the shuffle function.

def shuffle_(data) -> list:
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


print(shuffle_([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


# C-1.21) Write a Python program that repeatedly reads lines from standard input
#   until an EOFError is raised, and then outputs those lines in reverse order
#   (a user can indicate end of input by typing ctrl-D).

# Solve later


# C-1.22) Write a short Python program that takes two arrays a and b of length n
#   storing int values, and returns the dot product of a and b. That is, it returns
#   an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n− 1.

a = array('i', [1, 2, 3])
b = array('i', [4, 5, 6])
c = array('i', [])

for i in range(len(a)):
    temp = (a[i] * b[i])
    c.insert(i, temp)

print(c)


# C-1.23) Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds.
#   If that index is out of bounds, the program should catch the exception that results, and
#   print the following error message: “Don’t try buffer overflow attacks in Python!”

list2 = []
try:
    list2[3] = 10
except IndexError:
    print("Don’t try buffer overflow attacks in Python!")


# C-1.24) Write a short Python function that counts the number of vowels in a given character string.

def count_vowel(sample_string: str) -> int:
    """Counts the number of vowel in a given string

    Args:
        sample_string (str): Given character string

    Returns:
        int: Number of vowels in given string
    """
    vowel_count = 0
    for char in sample_string:
        if char in ["a", 'e', 'o', 'i', 'u']:
            vowel_count += 1
    return vowel_count


print(count_vowel("Mississippi river is drying up"))


# C-1.25) Write a short Python function that takes a string s, representing a sentence, and returns a copy of the string
#   with all punctuation removed. For example, if given the string "Let's try, Mike.", this function would return "Lets try Mike".

def remove_punc(sample_string: str) -> str:
    punc = '''!()-[]/{/};:'"\,<>./?@#$%^&*_~'''
    for char in sample_string:
        if char in punc:
            sample_string = sample_string.replace(char, "")

    return sample_string


print(remove_punc("Let's try, Mike."))


# C-1.26) Write a short program that takes as input three integers, a, b, and c, from
#   the console and determines if they can be used in a correct arithmetic
#   formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”

a = int(input("Enter 'a': "))
b = int(input("Enter 'b': "))
c = int(input("Enter 'c': "))
if a + b == c:
    print("Yes, it can be used in formula 'a + b = c'.")
elif b - c == a:
    print("Yes, it can be used in formula 'a = b - c'.")
elif a * b == c:
    print("Yes, it can be used in formula 'a * b = c'.")
else:
    print("No, it can be used in any formula.")


# C-1.27) In Section 1.8, we provided three different implementations of a generator that computes factors of a given integer.
#   The third of those implementations, from page 41, was the most efficient, but we noted that it did not yield the factors in
#   increasing order. Modify the generator so that it reports factors in increasing order, while maintaining its general performance advantages.

def factors(n):         # generator that computes factors
    k = 1
    while k * k < n:      # while k < sqrt(n)
        if n % k == 0:
            yield k
            k += 1
        if k * k == n:    # special case if n is perfect square
            yield k
    while k * k < n:      # while k < sqrt(n)
        if n % k == 0:
            yield n//k
            k += 1


# C-1.28) The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is defined as ||v|| = p root(v1**p + v2**p + ··· + vn**p).
#   For the special case of p = 2, this results in the traditional Euclidean norm, which represents the length of the vector.
#   For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a
#   Euclidean norm of sqrt(4**2 + 3**2) = sqrt(16 + 9) = √25 = 5. Give an implementation of a function named norm such that norm(v, p) returns the p-norm
#   value of v and norm(v) returns the Euclidean norm of v. You may assume that v is a list of numbers.

def norm(v: list, p=2) -> float:
    assert len(v) >= 2, "v should contain atleast 2 positive numbers"
    assert len(v) == p, "Dimensions should match the number of coordinates"
    result = 0
    for i in range(0, p):
        result += v[i]**p
    result = result**(1/p)
    return result
