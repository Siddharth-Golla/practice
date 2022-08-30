"""
You manage an amusement park, and you have a map that stores dates and attendance.

attendance = {
    "23 Sept": 2837,
    "24 Sept": 3726,
    "25 Sept": 6253,
}

Add a value for 26 Sept of 3333 people.
How many people attended in total on 25 and 26 Sept?
Is Data for 22 Sept available?
"""

attendance = {
    "23 Sept": 2837,
    "24 Sept": 3726,
    "25 Sept": 6253,
}

attendance["26 Sept"] = 3333
print("The number of people that attended on 25th and 26th Sept :", str(attendance["25 Sept"] + attendance["26 Sept"]))
print("Is data available for 22 Sept? ", "Yes" if "22 Sept" in attendance else "No")
