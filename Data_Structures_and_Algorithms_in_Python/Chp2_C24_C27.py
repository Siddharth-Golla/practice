# C-2.25) Exercise R-2.12 uses the __mul__ method to support multiplying a Vector by a number, while Exercise R-2.14
#   uses the __mul__ method to support computing a dot product of two vectors. Give a single implementation of Vector.__mul__
#   that uses run-time type checking to support both syntaxes u*v and u*k, where u and v designate vector instances and k represents a number.

# Solution done in Chp2_R9-R15.py file

# C-2.26) The SequenceIterator class of Section 2.3.4 provides what is known as a forward iterator. Implement a class named ReversedSequenceIterator that
#   serves as a reverse iterator for any Python sequence type. The first call to next should return the last element of the sequence, the second call to next
#   should return the second-to-last element, and so forth.

class ReverseSequenceIterator:
    """A reverse iterator for any of Python's sequence type"""

    def __init__(self, sequence) -> None:
        """Create a reverse iterator for the given sequence"""
        self._seq = sequence                                        # Keep a reference for the underlying data
        self._k = 0

    def __next__(self):
        """Return the previous element or else raise StopIteration error"""
        self._k -= 1                                                # Advance to previous element
        if abs(self._k) <= len(self._seq):
            # return the data element
            return (self._seq[self._k])
        else:
            # there are no more elements
            raise StopIteration()

    def __iter__(self):
        return self


if __name__ == '__main__':
    list1 = ReverseSequenceIterator([1, 2, 3, 4, 5, 6, 7, 8, 9])

    for i in range(9):
        print(list1.__next__())
