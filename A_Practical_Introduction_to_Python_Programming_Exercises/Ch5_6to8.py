"""
6) A number is called a perfect number if it is equal to the sum of all of its divisors, not including
the number itself. For instance, 6 is a perfect number because the divisors of 6 are 1, 2, 3, 6
and 6 = 1 + 2 + 3. As another example, 28 is a perfect number because its divisors are 1, 2, 4,
7, 14, 28 and 28 = 1 + 2 + 4 + 7 + 14. However, 15 is not a perfect number because its divisors
are 1, 3, 5, 15 and 15 6= 1 + 3 + 5. Write a program that finds all four of the perfect numbers
that are less than 10000.
"""

print("The perfect numbers less than 1000 are", end=" ")
for num in range(1,10000):
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum = divisor_sum + i

    if divisor_sum == num:
        print(num, end=" ")


"""
7) An integer is called squarefree if it is not divisible by any perfect squares other than 1. For
instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those
numbers (except 1) is a perfect square. On the other hand, 45 is not squarefree because it is
divisible by 9, which is a perfect square. Write a program that asks the user for an integer and
tells them if it is squarefree or not.
"""

number = int(input("Enter a number: "))
flag = False
for i in range(number, 1, -1):
    if number % i == 0 and flag == False:
        square = 2
        while square ** 2 < number:
            if i == square ** 2:
                flag = True
                break
            square = square + 1
if flag:
    print(f"{number} is not a squarefree number.")
else:
    print(f"{number} is a squarefree number.")


"""
8) Write a program that swaps the values of three variables x , y, and z, so that x gets the value
of y, y gets the value of z, and z gets the value of x .
"""
x = 10
y = 20
z = 30
print(x, y, z)
x, y, z = y, z, x
print(x, y, z)