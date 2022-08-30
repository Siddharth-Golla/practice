"""
10) Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be. [Hint: print('*'*10) prints ten asterisks.]

************
************
************
************

"""
# box_height = int(input("Enter the height of the box: "))
# box_width = int(input("Enter the width of the box: "))
# for i in range(box_height):
#     print("*" * box_width)


"""
11) Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be.

*******************
*                 *
*                 *
*******************

"""
# b_box_h = int(input("Enter the height of the border box: "))
# b_box_w = int(input("Enter the width of the border box: "))
# print("*" * b_box_w)
# for _ in range(b_box_h - 2):
#     print("*"," " * (b_box_w - 2),"*", sep="")
# print("*" * b_box_w)


"""
12) Use a for loop to print a triangle like the one below. Allow the user to specify how high the
triangle should be.

*
**
***
****
*****

"""
# tri_height1 = int(input("Enter the height of the triangle: "))
# for i in range(1, tri_height1 + 1):
#     print("*" * i)


"""
13) Use a for loop to print a triangle like the one below. Allow the user to specify how high the
triangle should be.

*****
****
***
**
*

"""


from math import ceil
tri_height2 = int(input("Enter the height of the triangle: "))
for i in range(tri_height2, 0, -1):
    print("*" * i)


"""
14) Use a for loop to print a diamond like the one below. Allow the user to specify how high the
diamond should be.

   *
  ***
 *****
*******
 *****
  ***
   *

"""

diamond_height = int(input("Enter the height of the diamond: "))

for i in range(1, (ceil(diamond_height/2)) + 1):
    print(("*" * (i+i - 1)).center(diamond_height))

# Solution pending