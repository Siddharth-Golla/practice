"""
4) Write a Python program to read a file line by line and store it into a list.
"""

file = open('sample.txt', 'r')
lines = file.readlines()
print(lines)
file.close()