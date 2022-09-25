# Arbitrary Arguments
"""
Create a function that takes an integer variable "count" and arbitrary number of
client names. Print out "count" hello messages for each client.

i.e. if count = 3, print out 3 hello messages for each client.
"""

def greetings(*clients, count:int = 1):
    for client in clients:
        for _ in range(count):
            print(f"Hello {client}")

if __name__ == '__main__':
    greetings("Bob")
    greetings("Clyde", count = 4)
    greetings("Mary", "Tom", "John")
    greetings("Syd", "Henry", count = 5)