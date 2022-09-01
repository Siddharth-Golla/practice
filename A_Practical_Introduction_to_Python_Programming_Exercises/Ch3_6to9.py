"""
6) Write a program that asks the user to enter two numbers, x and y, and computes |(x-y)/(x+y)|
"""
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
result = (abs(x - y)/(x + y))
print(result)


"""
7) Write a program that asks the user to enter an angle between -180◦
and 180◦ Using an expression with the modulo operator, convert the angle to its equivalent between 0 and 360 degree.
"""
angle = int(input("Enter angle between -180 to 180 degree: "))
if angle == 180:
    print("360")
else:
    print((angle + 180) % 360)


"""
8) Write a program that asks the user for a number of seconds and prints out how many minutes
and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds.
[Hint: Use the // operator to get minutes and the % operator to get seconds.]
"""

total_seconds = int(input("Enter number of seconds: "))
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f"The time is {minutes} minutes and {seconds} seconds")


"""
9) Write a program that asks the user for an hour between 1 and 12 and for how many hours in
the future they want to go. Print out what the hour will be that many hours into the future.
An example is shown below.
Enter hour: 8
How many hours ahead? 5
New hour: 1 o'clock
"""

hours = int(input("Enter hour: "))
plus_hours = int(input("How many hours ahead? "))
new_hour = (hours + plus_hours) % 12
if new_hour == 0:
    print(f"New Hour: 12 o'clock")
else:
    print(f"New Hour: {new_hour} o'clock")