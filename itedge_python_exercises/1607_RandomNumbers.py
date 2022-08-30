"""A car is driving at a speed of 67 km per hour.
Generate a random number between 1 and 1000 and store it in a variable kilometers.
This is the number of kilometers the car has driven.
How long did it take to drive that distance? Print out the result. 
"""

import random

# five instances shown
for _ in range(5):
    kilometers = random.randint(1,1000)
    speed = 67
    hours = kilometers // speed
    minutes = kilometers % speed
    print(f"Driving {kilometers} kilometers at a speed of {speed} km/hr took {hours} hours and {minutes} minutes.")
