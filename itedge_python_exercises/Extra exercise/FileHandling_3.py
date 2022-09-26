"""
3) Write a Python program to append text to a file and display the text.
"""
file = open('file.txt', 'a')
file.write("This is the appended text.\n")
file.close()

file = open("file.txt", "r")
print(file.read())
file.close()