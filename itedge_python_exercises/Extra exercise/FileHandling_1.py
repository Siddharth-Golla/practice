"""
1) Write a Python program to read an entire text file.
"""

file = open('sample.txt', 'r')
print(file.read())
file.close()