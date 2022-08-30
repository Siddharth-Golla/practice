

from dataclasses import replace
from random import choice, randint, randrange, sample


class Ecosystem:
    def __init__(self):
        river = []
        for i in range(11):
            river.append(
                Bear(randint(1, 15), choice(["Male", "Female"]), i))
        print(river)
        if river[0].move() == -1:
            river[0 - 1], river[0] = river[0], None
        elif river[0].move() == 1:
            river[0 + 1], river[0] = river[0], None
        else:
            pass
        print(river)


class Animal():
    def __init__(self, strength, gender):
        self.strength = strength
        self.gender = gender

    def __repr__(self):
        return f"{self.type}({self.strength}, {self.gender}, Pos:{self.position})"

    def move(self):
        return randint(-1, 1)


class Bear(Animal):
    def __init__(self, strength, gender, position):
        super().__init__(strength, gender)
        self.type = "Bear"
        self.position = position


class Fish(Animal):
    def __init__(self, strength, gender):
        super().__init__(strength, gender)
        self.type = "Fish"


if __name__ == '__main__':
    eco = Ecosystem()
    eco
