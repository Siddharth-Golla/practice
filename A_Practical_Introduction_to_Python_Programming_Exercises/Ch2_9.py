"""
9) The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
number thereafter is the sum of the two preceding numbers. Write a program that asks the
user how many Fibonacci numbers to print and then prints that many.

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 . . .

"""

prev = 0
current = 1
for i in range(50):
    print(current, end=", ")
    next = prev + current
    prev = current
    current = next