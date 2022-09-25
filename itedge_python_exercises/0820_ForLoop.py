# For loops
"""
Print out all the numbers from 0 to 100, their squares and their cubes, seperated by single space.
"""
for i in range(0,101):
    print(i, i ** 2, i ** 3)


"""
Ask the user for a number.
Print out a square matrik of the size indicated by the number
Inside each cell, print out 1 emoji
😀 - If row*column is divisible by 3
🤨 - If row*column % 3 = 1
😱 - If row*column % 3 = 2
"""

number = int(input("Enter a number: "))
for i in range(1,number + 1):
    print()
    for j in range(1, number + 1):
        if i * j % 3 == 0:
            print("\U0001F600", end=" ")
        if i * j % 3 == 1:
            print("\U0001F928", end=" ")
        if i * j % 3 == 2:
            print("\U0001F631", end=" ")
            