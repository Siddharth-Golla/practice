"""
8) A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Write a program that asks the user for a year and prints
out whether it is a leap year or not.
"""

# A year is a leap year if the following conditions are satisfied: 
# The year is multiple of 400.
# The year is multiple of 4 and not multiple of 100.

year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year.")
elif (year % 4 ==0) and (year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a  leap year.")


"""
9) Write a program that asks the user to enter a number and prints out all the divisors of that
number.
"""

num = 10 #int(input("Enter a number: "))
print(f"The divisors of {num} are", end=" ")
for divisor in range(1, num + 1):
    if num % divisor == 0:
        print(divisor, end=" ")

