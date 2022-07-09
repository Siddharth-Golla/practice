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

def make_change(amount_charged: int, amount_given: int):
    difference = amount_given - amount_charged
    no_of_thousand = 0
    no_of_five_hundred = 0
    no_of_two_hundred = 0
    no_of_hundred = 0
    no_of_fifty = 0
    no_of_twenty = 0
    no_of_ten = 0
    no_of_five = 0
    no_of_one = 0
    while difference:
        if difference > 1000:
            no_of_thousand += difference // 1000
            difference -= 1000 * no_of_thousand
        elif difference > 500:
            no_of_five_hundred += difference // 500
            difference -= 500 * no_of_five_hundred
        elif difference > 200:
            no_of_two_hundred = difference // 200
            difference -= 200 * no_of_two_hundred
        elif difference > 100:
            no_of_hundred = difference // 100
            difference -= 100 * no_of_hundred
        elif difference > 50:
            no_of_fifty = difference // 50
            difference -= 50 * no_of_fifty
        elif difference > 20:
            no_of_twenty = difference // 20
            difference -= 20 * no_of_twenty
        elif difference > 10:
            no_of_ten = difference // 10
            difference -= 10 * no_of_ten
        elif difference > 5:
            no_of_five = difference // 5
            difference -= 5 * no_of_five
        elif 0 <= difference < 5:
            no_of_one = difference
            difference -= no_of_one
        elif difference < 0:
            raise ValueError(
                "The amount given should not be less than amount charged")

    print(f"""
            1000 : {no_of_thousand},
            500 : {no_of_five_hundred},
            200 : {no_of_two_hundred},
            100 : {no_of_hundred},
            50 : {no_of_fifty},
            20 : {no_of_twenty},
            10 : {no_of_ten},
            5 : {no_of_five},
            1 : {no_of_one},
    """)


make_change(1, 2000)

# P-31) Write a Python program that can simulate a simple calculator, using the console as the exclusive input and output device.
#   That is, each input to the calculator, be it a number, like 12.34 or 1034, or an operator, like + or =, can be done on a separate line.
#   After each such input, you should output to the Python console what would be displayed on your calculator.


result = 0
number = eval(input(""))
result = number
operation = input("")
while operation != "=":
    if operation == "+":
        number2 = eval(input(""))
        result += number2
        print(result)
        operation = input("")
    if operation == "-":
        number2 = eval(input(""))
        result -= number2
        print(result)
        operation = input("")
    if operation == "*":
        number2 = eval(input(""))
        result *= number2
        print(result)
        operation = input("")
    if operation == "/":
        number2 = eval(input(""))
        result /= number2
        print(result)
        operation = input("")

if operation == "=":
    print(result)
