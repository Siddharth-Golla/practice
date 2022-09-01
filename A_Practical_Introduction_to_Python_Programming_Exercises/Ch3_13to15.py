from math import sin,cos,tan,radians
"""
13. Write a program that asks the user for a number and then prints out the sine, cosine, and
tangent of that number.
"""
angle_degree = int(input("Enter an angle: "))
print(f"The sine, cosine, and tangent of the angle {angle_degree} are {sin(radians(angle_degree))},{cos(radians(angle_degree))},{tan(radians(angle_degree))} respectively")



"""
14. Write a program that asks the user to enter an angle in degrees and prints out the sine of that
angle.
"""
angle_degree2 = int(input("Enter an angle in degree: "))
print(f"The sine of the angle {angle_degree2} degree is {sin(radians(angle_degree2))}")


"""
15. Write a program that prints out the sine and cosine of the angles ranging from 0 to 345◦
in 15◦ increments. Each result should be rounded to 4 decimal places. Sample output is shown below:
0 --- 0.0 1.0
15 --- 0.2588 0.9659
30 --- 0.5 0.866
...
345 --- -0.2588 0.9659

"""

for i in range(0, 346, 15):
    print(f"{i} --- {round(sin(radians(i)), 4)} {round(cos(radians(i)), 4)}")