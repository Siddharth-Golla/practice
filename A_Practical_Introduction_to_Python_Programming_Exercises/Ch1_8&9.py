"""
8) Write a program that asks the user to enter three numbers (use three separate input statements).
Create variables called total and average that hold the sum and average of the
three numbers and print out the values of total and average.
"""

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))
total = first_number + second_number + third_number
average = total / 3
print("The total is", total, "and the average is", average)


"""
9) A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
the percent tip they want to leave. Then print both the tip amount and the total bill with the
tip included.
"""

price = eval(input("Enter the price of the meal: "))
tip = price * (int(input("Enter the tip percentage (0-100): ")))/100
print("The total bill is", price + tip, "with a tip of", tip)