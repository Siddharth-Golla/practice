"""
10) (a) One way to find out the last digit of a number is to mod the number by 10. Write a
program that asks the user to enter a power. Then find the last digit of 2 raised to that
power.
(b) One way to find out the last two digits of a number is to mod the number by 100. Write
a program that asks the user to enter a power. Then find the last two digits of 2 raised to
that power.
(c) Write a program that asks the user to enter a power and how many digits they want.
Find the last that many digits of 2 raised to the power the user entered.
(Summing up the three questions in one solution)
"""

power = int(input("Enter a power: "))
digits = int(input("Enter the number of digits: "))
last_digit = (2 ** power) % 10
last_2_digit = (2 ** power) % 100
last_n_digit = (2 ** power) % (10 ** digits)
print(f"The last digit is {last_digit}")
print(f"The last 2 digit are {last_2_digit}")
print(f"The last {digits} digits are {last_n_digit}")


"""
11) Write a program that asks the user to enter a weight in kilograms. The program should
convert it to pounds, printing the answer rounded to the nearest tenth of a pound.
"""
weight_in_kg = int(input("Enter weight in kilograms: "))
weight_in_pounds = (weight_in_kg * 2.205)
print(f"The weight in pounds is {round(weight_in_pounds, 1)} lbs.")


"""
12) Write a program that asks the user for a number and prints out the factorial of that number.
"""
num = int(input("Enter a number: "))
fact = 1
for i in range(num, 0, -1):
    fact = fact * i

print(f"The factorial of the number {num} is {fact}")