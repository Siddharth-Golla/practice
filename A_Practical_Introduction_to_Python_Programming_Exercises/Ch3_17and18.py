"""
17) A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator,
determine how many leap years there have been between 1600 and that year.
"""

user_year = int(input("Enter a year: "))
years = (user_year - 1600)                                                  # total number of years between 1601 to user_year
leap_year_count = (years // 4) - (years // 100) + (years // 400) + 1        # +1 to add leap year of 1600
print(leap_year_count)



"""
18) Write a program that given an amount of change less than $1.00 will print out exactly how
many quarters, dimes, nickels, and pennies will be needed to efficiently make that change.
[Hint: the // operator may be useful.]
"""

amount = int(input("Enter amount in cents(e.g 75): "))
difference = amount
while difference:
    quarters = difference // 25
    difference = difference - (quarters * 25)
    dimes = difference // 10
    difference = difference - (dimes * 10)
    nickels = difference // 10
    difference = difference - (nickels * 5)
    pennies = difference
    difference = difference - pennies

print(f"The change is {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies.")