# Keyword Arguments
"""
A pet shelter has cats, dogs and bunnies.

Create a function that takes the number of each type that are available and
prints out a string detailing how many pets there are
"""

def shelter(cats:int = 0, dogs:int = 0, bunnies:int = 0):
    if not cats and not dogs and not bunnies:
        print("No animals are at the shelter. Thank you for adopting all.")
    else:
        print("We have")
        if cats:
            print(f"{cats} cats")
        if dogs:
            print(f"{dogs} dogs")
        if bunnies:
            print(f"{bunnies} bunnies")


if __name__ == '__main__':
    shelter(dogs = 2, bunnies=3)
    shelter(4, 3, 5)
    shelter(2)
    shelter()
    
