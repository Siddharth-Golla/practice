"""
6) Write a Python program to copy the contents of a file to another file.
"""

file = open('sample.txt', 'r')
content = file.read()
file2 = open('sample2.txt', 'w')
file2.write(content)
file.close()
file2.close()