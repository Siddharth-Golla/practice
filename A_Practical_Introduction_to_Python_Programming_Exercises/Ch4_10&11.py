"""
10) Write a multiplication game program for kids. The program should give the player ten randomly generated multiplication questions to do. After each, the program should tell them
whether they got it right or wrong and what the correct answer is.
"""

from random import randint

for i in range(1,11):
    num1 = randint(1,10)
    num2 = randint(1,10)
    print(f"Question {i}: {num1} x {num2} = ", end="")
    result = int(input())
    if result == num1 * num2:
        print("You got it right!")
    else:
        print(f"Wrong! The correct answer is {num1 * num2}")



"""
11) Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
and asks them how many hours into the future they want to go. Print out what the hour will
be that many hours into the future, printing am or pm as appropriate. An example is shown
below.
"""
user = eval(input("Enter hour: "))
day = input("enter am (1) or pm (2): ")
hour = eval(input("How many hours ahead ? "))

# Transform the user time to 24Hr format
if day == 'pm' and user != 12:
    user += 12
elif day == 'am' and user == 12:
    user = 0

# Add the future hours
new_hour = user + hour

# new_hour holds the result in 24 format. Transform back to am pm format.
new_hour = new_hour % 24
if new_hour >= 0 and new_hour < 12:         # If : 0 < new_hour < 12 then print AM else print PM
    new_hour = new_hour % 12 ;
    if new_hour == 0:
        new_hour = 12;
    print(f"New hour : {new_hour} ", end="am")
    print()
else:
    new_hour = new_hour % 12;
    if new_hour == 0:
        new_hour = 12 ;
    print(f"New hour : {new_hour} ", end="pm")
    print()

