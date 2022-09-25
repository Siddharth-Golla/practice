"""
Program to create the multiplication table (from 1 to 10) of a number.
"""

number = int(input("Enter a number to create multiplication table: "))

for i in range(1,11):
    print(f"{i} x {number} = {i*number}")