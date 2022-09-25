# Nested Functions
"""
Create a function that takes a disctionary of users and their bank balance.
Inside, create a function that takes a number and returns its double.
Double each user's bank balance and print out a statement
"""

def balance(users:dict):
    def doubles(number):
        return number + number

    for user in users:
        users[user] = doubles(users[user])
        print(f"User {user} has ${users[user]} in account.")



if __name__ == '__main__':
    users = {
        "Alice" : 10000,
        "Bob" : 5000,
        "Carol" : 7000,
        "Dan" : 9000
    }
    balance(users)
