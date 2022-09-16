"""
3. Write a program that asks the user to enter a value n, and then computes (1+
1/2 +1/3 +···+1/n) - ln(n). The ln function is log in the math module.
"""
from math import log

num = int(input("Enter a number: "))
result = 1
for i in range(2, num + 1):
    result = result + (1/i)
result = result - log(num)
print(result)

"""
4. Write a program to compute the sum (1 - 2 + 3 - 4 + ··· + 1999 - 2000).
"""
sum1 = 0
sum2 = 0
for i in range(1,2001,2):
    sum1 = sum1 + i
for i in range(2,2001,2):
    sum2 = sum2 + i

print("Sum is ", sum1 - sum2)

"""
5. Write a program that asks the user to enter a number and prints the sum of the divisors of
that number. The sum of the divisors of a number is an important function in number theory.
"""
user_num = int(input("Enter a number: "))
total = 0
for divisor in range(1, user_num):
    if user_num % divisor == 0:
        total = total + divisor
print(total)
