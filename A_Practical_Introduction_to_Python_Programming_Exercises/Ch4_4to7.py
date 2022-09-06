"""
4) Write a program that asks the user how many credits they have taken. If they have taken 23
or less, print that the student is a freshman. If they have taken between 24 and 53, print that
they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.
"""

from random import randint


credits = int(input("Enter your credits(0 or more): "))
if credits >= 84:
    print("Student is a senior.")
elif 53 < credits < 84:
    print("Student is a junior.")
elif 23 < credits < 54:
    print("Student is a sophomore.")
else:
    print("Student is a freshman.")


"""
5) Generate a random number between 1 and 10. Ask the user to guess the number and print a
message based on whether they get it right or not.
"""

number = randint(1, 10)
guess = int(input("Enter your guess(1 - 10)"))
if number == guess:
    print(f"You guessed right. The number is {number}.")
else:
    print(f"You guessed wrong. The correct guess is {number}")


"""
6) A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
program that asks the user how many items they are buying and prints the total cost.

"""

items = int(input("Enter the amount of items: "))
for items in range(103):
    print(items, end=" ")
    if items >= 100:
        print(f"The total cost is {items * 7} at the rate of $7 per item.")
    elif 10 <= items <= 99:
        print(f"The total cost is {items * 10} at the rate of $10 per item.")
    else:
        print(f"The total cost is {items * 12} at the rate of $12 per item.")


"""
7) Write a program that asks the user for two numbers and prints Close if the numbers are
within .001 of each other and Not close otherwise.
"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
diff = abs(num1 - num2)
print(diff)
if diff <= (1/100):
    print("Close")
else:
    print("Not close")
