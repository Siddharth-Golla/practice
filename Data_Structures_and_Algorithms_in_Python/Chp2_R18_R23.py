# R-2.18) Give a short fragment of Python code that uses the progression classes from Section 2.4.2
#   to find the 8th value of a Fibonacci progression that starts with 2 and 2 as its first two values.

# print("Fibonacci progression with start values 2 and 2:")
# FibonacciProgression(2, 2).print_progression(8)

# R-2.19) When using the ArithmeticProgression class of Section 2.4.2 with an increment of 128 and a start of 0,
#   how many calls to __next__ can we make before we reach an integer of 2**63 or larger?

# SOLUTION: 9 calls are to be made, since each call increments with 128 = 2**7; so 9 calls to 2**7 will give 2**63

# R-2.20) What are some potential efficiency disadvantages of having very deep inheritance trees, that is,
# a large set of classes, A, B, C, and so on, such that B extends A, C extends B, D extends C, etc.?


# R-2.21) What are some potential efficiency disadvantages of having very shallow inheritance trees, that is,
# a large set of classes, A, B, C, and so on, such that all of these classes extend a single class, Z?


# R-2.22) The collections.Sequence abstract base class does not provide support for comparing two sequences to each other.
# Modify our Sequence class from Code Fragment 2.14 to include a definition for the __eq__ method, so that expression seq1 == seq2 will return True
# precisely when the two sequences are element by element equivalent.

# R-2.23) In similar spirit to the previous problem, augment the Sequence class with method __lt__ , to support lexicographic comparison seq1 < seq2.

from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence"""

    def __contains__(self, val):
        """Return True if val found in sequence; False otherwise"""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def __eq__(self, other: object) -> bool:
        """Returns True if two sequences are element by element equivalent"""
        if len(self) == len(other):
            for j in range(len(self)):
                if self[j] != other[j]:
                    return False
            else:
                return False
        else:
            raise ValueError(
                "The two sequence compared are not of same length")

    def __lt__(self, other):
        """Return True if self is lexicographically less than other"""
        pass

    def index(self, val):
        """Returns the leftmost index at which val is found; otherwise raise a ValueError"""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError("Value not found in sequence")

    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
