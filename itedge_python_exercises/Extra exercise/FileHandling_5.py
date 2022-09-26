"""
5) Write a Python program to get the file size of a plain file.
"""

import os
 
file_size = os.path.getsize('sample.txt')
print("File Size: ", file_size, "bytes")