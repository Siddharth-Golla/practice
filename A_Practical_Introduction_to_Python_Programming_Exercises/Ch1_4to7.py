"""
4) Write a program that computes and prints the result of (512 - 282) / 47 · 48 + 5
It is roughly 0.1017.
"""

print((512 - 282) / ((47*48) + 5))


"""
5) Ask the user to enter a number. Print out the square of the number, but use the sep optional
argument to print it out in a full sentence that ends in a period.
"""

num = int(input("Enter a number: "))
print("The square of " + str(num) + " is " + str(num * num),".", sep="")


"""
6) Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x,
and 5x, each separated by three dashes, like below.

Enter a number: 7
7---14---21---28---35
"""

x = int(input("Enter x: "))
print(x, x*2, x*3, x*4, x*5, sep='---')


"""
7) Write a program that asks the user for a weight in kilograms and converts it to pounds. There
are 2.2 pounds in a kilogram.
"""

kilos = eval(input("Enter weight in kilos: "))
print("The weight in pounds is", kilos * 2.2, "pounds.")

