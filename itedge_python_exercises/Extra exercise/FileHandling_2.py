"""
2) Write a Python program to read first n lines of a file.
"""
n = 2
file = open('sample.txt', 'r')
for i in range(n):
    print(file.readline())
file.close()