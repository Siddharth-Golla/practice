# P-2.39) Develop an inheritance hierarchy based upon a Polygon class that has abstract methods area( ) and perimeter( ).
#   Implement classes Triangle, Quadrilateral, Pentagon, Hexagon, and Octagon that extend this base class, with the obvious meanings
#   for the area( ) and perimeter( ) methods.Also implement classes, IsoscelesTriangle, EquilateralTriangle, Rectangle, and Square,
#   that have the appropriate inheritance relationships. Finally, write a simple program that allows users to create polygons of the
#   various types and input their geometric dimensions, and the program then outputs their area and perimeter. For extra effort,
#   allow users to input polygons by specifying their vertex coordinates and be able to test if two such polygons are similar.


from math import sqrt


class Polygon:
    def __init__(self, vertice1: tuple, vertice2: tuple, vertice3: tuple) -> None:
        """Create an instance of polygon class with three vertices.

        Give the three vertices in co-ordinate form eg. (x1,y1)

        Args:
            vertice1 (x1: int,y1: int): A tuple containing x and y co-ordinate of vertice1
            vertice2 (x2: int,y2: int): A tuple containing x and y co-ordinate of vertice2
            vertice3 (x3: int,y3: int): A tuple containing x and y co-ordinate of vertice3
        """
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3
        self.x1 = vertice1[0]
        self.y1 = vertice1[1]
        self.x2 = vertice2[0]
        self.y2 = vertice2[1]
        self.x3 = vertice3[0]
        self.y3 = vertice3[1]

    def vertices(self):
        return f"({self.x1},{self.y1})({self.x2},{self.y2})({self.x3},{self.y3})"

    @staticmethod
    def calculate_side(x1, y1, x2, y2):
        return sqrt((abs(x2-x1)**2 + abs(y2-y1)**2))

    def side1(self):
        self.side1 = Polygon.calculate_side(self.x1, self.y1, self.x2, self.y2)
        return self.side1

    def side2(self):
        self.side2 = Polygon.calculate_side(self.x2, self.y2, self.x3, self.y3)
        return self.side2

    def side3(self):
        self.side3 = Polygon.calculate_side(self.x1, self.y1, self.x3, self.y3)
        return self.side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        self.area = sqrt(s * (s - self.side1) *
                         (s - self.side2)*(s - self.side3))
        return self.area

    def perimeter(self):
        peri = self.side1 + self.side2 + self.side3
        return peri


p = Polygon((0, 0), (4, 0), (0, 4))
print(p.side1(), p.side2(), p.side3(), p.area(), p.perimeter())
