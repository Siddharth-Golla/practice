"""
1) Write a program that asks the user to enter a length in centimeters. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program
should convert the length to inches and print out the result. There are 2.54 centimeters in an
inch.
"""

centimeters = int(input("Enter a length in centimeters: "))
if centimeters < 0:
    print("You entered an invalid input.")
else:
    inches = centimeters / 2.54
    print(f"The length in inche is {inches:.2f} inches")



"""
2) Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature is in.
Your program should convert the temperature to the other unit. The conversions are F = (9/5)C + 32 and C = 5/9(F - 32)
"""

temperature = int(input("Enter temperature: "))
unit = int(input("Enter 1 for Celsius or 2 for Fahrenheit: "))
if unit == 1:
    far_temp = ((9/5) * temperature) + 32
    print(f"The temperature in Fahrenheit is {far_temp}")
elif unit == 2:
    cel_temp = (temperature - 32) * (5/9)
    print(f"The temperature in Celsius is {cel_temp}")
else:
    print("You have entered wrong option.")




"""
3) Ask the user to enter a temperature in Celsius. The program should print a message based on the temperature:
• If the temperature is less than -273.15, print that the temperature is invalid because it is below absolute zero.
• If it is exactly -273.15, print that the temperature is absolute 0.
• If the temperature is between -273.15 and 0, print that the temperature is below freezing.
• If it is 0, print that the temperature is at the freezing point.
• If it is between 0 and 100, print that the temperature is in the normal range.
• If it is 100, print that the temperature is at the boiling point.
• If it is above 100, print that the temperature is above the boiling point
"""

temp = int(input("Enter temperature in Celsius: "))
if temp > 100:
    print("The temperature is above boling point.")
elif temp == 100:
    print("The temperature is at boiling point.")
elif 0 < temp < 100:
    print("The temperature is in the normal range.")
elif temp == 0:
    print("The temperature is at freezing level.")
elif -273.15 < temp < 0:
    print("The temperature is below freezing level.")
elif temp == -273.15:
    print("The temperature is at absolute zero.")
else:
    print("The temperature is invalid because it is below absolute zero.")
