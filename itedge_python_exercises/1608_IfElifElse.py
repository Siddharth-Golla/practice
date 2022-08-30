"""
You receive a message from a remote server, as a 3 digit error code.
You have this code in a variable.

response = 404

If the message ends with 0              -> print "Bad request"
If the message ends with 1              -> print "Unauthorised"
If the message ends with 2              -> print "Payement required"
If the message ends with 3              -> print "Forbidden"
If the message ends with 4              -> print "Not Found"
If the message ends with anything else  -> print "Unknown"
"""

response = 404
last_digit = response % 10
if last_digit == 0:
    print("Bad request")
elif last_digit == 1:
    print("Unauthorised")
elif last_digit == 2:
    print("Payement required")
elif last_digit == 3:
    print("Forbidden")
elif last_digit == 4:
    print("Not Found")
else:
    print("Unknown")


"""
2) You are designing a grading system for school exams.
THe total for an exam is 100 points, you need to convert that into a grade A to F.
Design a program that reads in a number that represents a student's grade, from 1 to 100 and prints it.

"""

points = int(input("Enter the points of the exam: "))
grade = ""
if 90 <= points <= 100:
    grade = "A"
elif 80 <= points <= 89:
    grade = "B"
elif 70 <= points <= 79:
    grade = "C"
elif 60 <= points <= 69:
    grade = "D"
elif 50 <= points <= 59:
    grade = "E"
else:
    grade = "F"

print(f"The grade is {grade}")