"""
5) Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, . . . , 83, 86, 89.
"""

for i in range(8,90,3):
    print(i)


"""
6) Write a program that uses a for loop to print the numbers 100, 98, 96, . . . , 4, 2.
"""

for i in range(100,1,-2):
    print(i)


"""
7) Write a program that uses exactly four for loops to print the sequence of letters below.

AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG
"""

for _ in range(10):
    print("A", end="")
for _ in range(7):
    print("B", end="")
for _ in range(4):
    print("CD", end="")
print("E", end="")
for _ in range(6):
    print("F", end="")
print("G")


"""
8) Write a program that asks the user for their name and how many times to print it.
The program should print out the user's name the specified number of times.
"""

name = input("Enter your name: ")
number = int(input("Enter number of times it should print: "))
for _ in range(number):
    print(name)

