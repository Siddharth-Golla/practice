"""
19) Write a program that draws “modular rectangles” like the ones below. The user specifies the
width and height of the rectangle, and the entries start at 0 and increase typewriter fashion
from left to right and top to bottom, but are all done mod 10. Below are examples of a 3 x 5
rectangle and a 4 x 8.

0 1 2 3 4
5 6 7 8 9
0 1 2 3 4

0 1 2 3 4 5 6 7
8 9 0 1 2 3 4 5
6 7 8 9 0 1 2 3
4 5 6 7 8 9 0 1
"""

width = int(input("Enter width of rect: "))
height = int(input("Enter height of rect: "))
counter = 0
for i in range(height):
    for j in range(width):
        print(counter%10, end=" ")
        counter += 1
    print()