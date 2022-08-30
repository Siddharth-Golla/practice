# R-2.9) Implement the __sub__ method for the Vector class of Section 2.3.3, so that
#   the expression u-v returns a new vector instance representing the difference between two vectors.

# R-2.10) Implement the __neg__ method for the Vector class of Section 2.3.3, so that
#   the expression -v returns a new vector instance whose coordinates are all the negated values of the respective coordinates of v.

# R-2.11) In Section 2.3.3, we note that our Vector class supports a syntax such as v = u + [5, 3, 10, -2, 1],
#   in which the sum of a vector and list returns a new vector. However, the syntax v = [5, 3, 10, -2, 1] + u is illegal.
#   Explain how the Vector class definition can be revised so that this syntax generates a new vector.

# R-2.12) Implement the __mul__ method for the Vector class of Section 2.3.3, so that the expression v * 3 returns a new vector with coordinates that are 3
#   times the respective coordinates of v.

# R-2.13) Exercise R-2.12 asks for an implementation of __mul__ , for the Vector class of Section 2.3.3, to provide support for the syntax v * 3.
#   Implement the __rmul__ method, to provide additional support for syntax 3 * v.

# R-2.14) Implement the __mul__ method for the Vector class of Section 2.3.3, so that the expression u * v returns a scalar that represents the dot product of
# the vectors, that is, ∑di=1 ui · vi

# R-2.15) The Vector class of Section 2.3.3 provides a constructor that takes an integer d, and produces a d-dimensional vector with all coordinates equal to 0.
#   Another convenient form for creating a new vector would be to send the constructor a parameter that is some iterable type representing a sequence of numbers,
#   and to create a vector with dimension equal to the length of that sequence and coordinates equal to the sequence values.
#   For example, Vector([4, 7, 5]) would produce a three-dimensional vector with coordinates <4, 7, 5>.
#   Modify the constructor so that either of these forms is acceptable; that is, if a single integer is sent, it produces a vector of that
#   dimension with all zeros, but if a sequence of numbers is provided, it produces a vector with coordinates based on that sequence.

# All questions solved by revising the Vector Class from the book


from typing import Sequence


class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros.

        Args:
            d ([int]): No of dimensions of the vector
        """
        if isinstance(d, int):
            self._coords = [0] * d

        if isinstance(d, Sequence):
            self._coords = [0] * len(d)
            for i in range(len(d)):
                self._coords[i] = d[i]

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords[0:]) + '>'                # The book representation doesnt show all the coordinates; this way it does

    def __sub__(self, other):
        """Return difference of two vectors."""
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        """Return a new vector with values negated"""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -abs(self[j])
        return result

    def __radd__(self, other):
        """Return sum of two vectors.

            This is the right add implementation which supports b.add(a).
        """
        if len(self) != len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other[j] + self[j]
        return result

    def __mul__(self, other):
        """Return a new Vector if the other param is instance of int
            else return the dot product of two vectors if the other param is a Vector
        """
        if isinstance(other, int):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
        elif isinstance(other, Vector):
            result = 0
            for j in range(len(self)):
                result += self[j] * other[j]
        else:
            raise ValueError('Invalid Input')

        return result

    def __rmul__(self, other):
        """
            This is the right multiplication implementation.

        """

        if isinstance(other, int):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
        elif isinstance(other, Vector):
            result = 0
            for j in range(len(self)):
                result += self[j] * other[j]
        else:
            raise ValueError('Invalid Input')

        return result


if __name__ == '__main__':
    vector1 = Vector(3)
    vector2 = Vector(3)
    vector3 = Vector([5, 3, 4])
    for i in range(0, 3):
        vector1[i] = i
        vector2[i] = 2 * i

    print(vector1)
    print(vector2)
    print(vector1 + vector2)
    print(vector2 - vector1)
    print(vector1 * 2)
    print(3 * vector2)
    print(vector1 * vector2)
    print(vector3)
