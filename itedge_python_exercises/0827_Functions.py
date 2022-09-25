"""
Design a function that asks user's name. Then it asks for user's birth year.
Finally it prints out a message saying the user's name and age.
Call the function 3 times.
"""

def foo():
    current_year = 2022
    name = input("Enter your name: ")
    birth_year = int(input("Enter your birth year(yyyy): "))
    print(f"Hello {name}. In the year {current_year} you will be {current_year - birth_year} years old.")



"""
Create a function that receives the name of an animal, and returns the estimated lifespan.
cat             ->  15
dog             ->  10
rabbit          ->  12
everything else ->  20
Ask the user to input an animal, then print out the estimated lifespan of that animal.
"""

def lifespan(animal:str):
    if animal.lower() == "cat":
        return f"A {animal} lives around 15 years"
    elif animal.lower() == "dog":
        return f"A {animal} lives around 10 years"
    elif animal.lower() == "rabbit":
        return f"A {animal} lives around 12 years"
    else:
        return f"A {animal} lives around 20 years"


if __name__ == "__main__":
    for _ in range(3):
        foo()

    animal = input("Enter an animal: ")
    print(lifespan(animal))