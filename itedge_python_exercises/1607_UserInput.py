"""Create a program that asks a user's birth year.
Take a future year in a variable future_year.
Then print out the user's estimated age in that year.
"""
birth_year = input("Enter your birth year: ")
future_year = input("Enter a future year to know the estimated age at that year: ")
estimated_age = int(future_year) - int(birth_year)
print(f"In the year {future_year} you will be {estimated_age} years old.")