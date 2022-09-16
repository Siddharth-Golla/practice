# Expressions
"""
Is following expression smaller than or greater than the number 86. Print the message to console.
(3 * (15 / 5 + 5) * 44 - 5 ** 3) // 16
"""

result = (3 * (15 / 5 + 5) * 44 - 5 ** 3) // 16
print("The number is greater than 86") if result > 86 else print("The number is smaller than 86")


# Ranges
"""
Ask a user to input their age.
If they are under 13, they are a child
If they are under 18, they are a teen
If they are older, they are adult

Using ranges print out the correct message.
"""
age = int(input("Enter your age: "))
if age in range(0,14):
    print("You are a child.")
elif age in range(14,19):
    print("You are a teen.")
else:
    print("You are an adult.")


# Truth Value testing
"""
You have won the lottery together with some friends, winning 1,000,000
Ask the user how many friends were involved and print how much each friend won.
Division by 0 causes an error, so you need to check that.
"""

winners = int(input("Enter the number of people involed in winning lottery: "))
if winners > 0:
    print(f"Each friend won {1000000/winners:.2f} amount.")
else:
    print("THe number of people winning the lottery cannot be 0 or less than 0.")