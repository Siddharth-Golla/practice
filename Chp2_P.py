# P-29) Write a Python program that outputs all possible strings formed by using
#   the characters c , a , t , d , o , and g exactly once.

#   Solve later using recursion


# P-30) Write a Python program that can take a positive integer greater than 2 as
#   input and write out the number of times one must repeatedly divide this
#   number by 2 before getting a value less than 2.

num = 128
count = 0
while num // 2 >= 2:
    num = num // 2
    count += 1


# P-31) Write a Python program that can “make change.” Your program should take two numbers as input,
#   one that is a monetary amount charged and the other that is a monetary amount given.
#   It should then return the number of each kind of bill and coin to give back as change for the difference between
#   the amount given and the amount charged. The values assigned to the bills and
#   coins can be based on the monetary system of any current or former government.
#   Try to design your program so that it returns as few bills and coins as possible
