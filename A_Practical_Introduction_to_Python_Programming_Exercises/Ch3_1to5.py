import random
"""
1) Write a program that generates and prints 50 random integers, each between 3 and 6
"""

for i in range(50):
    print(random.randint(3,6), end=" ")
print()



"""
2) Write a program that generates a random number, x, between 1 and 50, a random number y
between 2 and 5, and computes x ** y.
"""

x = random.randint(1,50)
y = random.randint(2,5)
print(f"{x}**{y} = ", x**y)


"""
3) Write a program that generates a random number between 1 and 10 and prints your name
that many times.
"""

for _ in range(random.randint(1,10)):
    print("Myname")


"""
4) Write a program that generates a random decimal number between 1 and 10 with two decimal
places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00.
"""

print(round(random.uniform(1,10), 2))


"""
5) Write a program that generates 50 random numbers such that the first number is between 1
and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last is between
1 and 51.
"""

for i in range(2,52):
    print(random.randint(1, i), end=" ")