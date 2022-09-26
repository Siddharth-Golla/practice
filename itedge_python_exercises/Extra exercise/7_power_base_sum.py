"""
2) Write a Python program to calculate the sum of all digits of the base to the specified power
Test Data:
If power_base_sum(2, 100)
Expected Output :
115
"""

def power_base_sum(base:int, power:int) -> int:
    result = 0
    total = base ** power
    digit_length = len(str(total))
    for _ in range(digit_length):
        result = result + total % 10
        total = total // 10
    return result

print(power_base_sum(2, 100))