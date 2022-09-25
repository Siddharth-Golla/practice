"""
Program to display the Fibonacci sequence up to n-th term where n is provided by the user.(Use while)
"""

n = int(input("Enter the n-th term to display fibonacci series: "))
first_num = 0
second_num = 1
print(first_num, second_num, end=" ")

while n > 2:
    result = first_num + second_num
    print(result, end=" ")
    first_num = second_num
    second_num = result
    n -= 1

print()