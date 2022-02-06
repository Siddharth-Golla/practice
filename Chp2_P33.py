# P-2.33) Write a Python program that inputs a polynomial in standard algebraic
#   notation and outputs the first derivative of that polynomial.

# ax**2 + bx + c

#
class Polynomial:
    def __init__(self, *coefficients):
        """Coefficients are in the form of a_n, a_n-1,..., a_1, a_0 where n is the degree of the term

        If a term of particular degree is not present in the polynomial then coefficient is 0
        """
        self._coefficients = list(coefficients)

    def __repr__(self) -> str:
        return "Polynomial"+str(tuple(self._coefficients))

    def __str__(self):

        def expr_term(degree):
            # Returns string of a single term without the coeff eg. x**2, x**4 , x
            if degree == 0:
                res = ""
            elif degree == 1:
                res = "x"
            else:
                res = "x**" + str(degree)
            return res

        degree = len(self._coefficients) - 1
        result = ""

        for i in range(degree + 1):
            coeff = self._coefficients[i]
            # if coeff is 1, then 1 should not appear before x; eg x instead of 1x
            if abs(coeff) == 1 and i < degree:
                result += f"{'+' if coeff > 0 else '-'}{expr_term(degree - i)}"
            # if coeff is not 1 or 0, then concatenate sign(+/-), coeff and term; eg '-7x**3'
            elif coeff != 0:
                result += f"{'+' if coeff > 0 else '-'}{abs(coeff)}{expr_term(degree - i)}"

        return result.lstrip("+")                   # Remove the leading '+'

    def first_derivative():
        pass


if __name__ == '__main__':
    p1 = Polynomial(1, 0, -4, 3, 0)
    p2 = Polynomial(2, 0)
    p3 = Polynomial(4, 1, -1)
    p4 = Polynomial(3, 0, -5, 2, 7)
    p5 = Polynomial(-42)

    print(p1)
    print(p2)
    print(p3)
    print(str(p4))
