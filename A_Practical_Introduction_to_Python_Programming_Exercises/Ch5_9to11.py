"""
9. Write a program to count how many integers from 1 to 1000 are not perfect squares, perfect
cubes, or perfect fifth powers.
"""
number = 1
perfect_square = 0
perfect_cube = 0
perfect_fifth = 0
while number ** 2 < 1001:
    perfect_square += 1
    number += 1
number = 1
while number ** 3 < 1001:
    perfect_cube += 1
    number += 1
number = 1
while number ** 5 < 1001:
    perfect_fifth += 1
    number += 1
print(f"The number of integers from 1 to 1000 that are not perfect squares, perfect cubes, or perfect fifth powers are {1000 - perfect_square},{1000 - perfect_cube} and {1000 - perfect_fifth} respectively.")

"""
10. Ask the user to enter 10 test scores. Write a program to do the following:
(a) Print out the highest and lowest scores.
(b) Print out the average of the scores.
(c) Print out the second largest score.
(d) If any of the scores is greater than 100, then after all the scores have been entered, print a message warning the user that a value over 100 has been entered.
(e) Drop the two lowest scores and print out the average of the rest of them.
"""
flag = False
largest = eval(input("Enter a positive number: "))
second_largest = eval(input("Enter a positive number: "))
if second_largest > largest:
    second_largest , largest = largest, second_largest
    smallest = second_largest
    second_smallest = largest
else:
    smallest = second_largest
    second_smallest = largest

if largest > 100 or second_largest > 100:
    flag = True
sum = largest + second_largest
for i in range(8):
    num = eval(input('Enter a positive number: '))
    if num > 100:
        flag = True
    sum = sum + num
    if num>largest:
        second_largest = largest
        largest = num
    if num < smallest:
        second_smallest = smallest
        smallest = num

print(f"The highest score is {largest}.")
print(f"The lowest score is {smallest}.")
print(f"The average is {sum/10}.")
print(f"The second largest score is {second_largest}.")
if flag:
    print("You have entered a score above 100.")
print(f"The average after dropping two lowest score is {(sum - (smallest + second_smallest))/8}.")


"""
11. Write a program that computes the factorial of a number. The factorial, n!, of a number n is the
product of all the integers between 1 and n, including n. For instance, 5! =1·2·3·4·5 =120.
"""
number = int(input("Enter a positive integer to find its factorial: "))
fact = 1
for i in range(2, number + 1):
    fact = fact * i
print(f"The factorial of {number} is {fact}.")