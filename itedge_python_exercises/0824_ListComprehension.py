# List Comprehension
"""
Generate a list of the truth values of these elements

el = [56, 0j, False, "run", '', [], ("Paris", )]
"""

el = [56, 0j, False, "run", '', [], ("Paris", )]

truth_values = [bool(x) for x in el]

print(truth_values)


# List comprehension with if
"""
You have a dictionary of party guests and their age
guests = {
        "Alice": 15,
        "Bob": 18,
        "Carol": 26,
        "Dan": 17,
        "Ellen": 22,
}
Generate a list of greetinds "Hello <guest_name>" for each guest that is atleast 18
years old. Print out the list.
"""

guests = {
    "Alice": 15,
    "Bob": 18,
    "Carol": 26,
    "Dan": 17,
    "Ellen": 22,
}

greetings = [f"Hello {x}" for x in guests if guests[x] > 17]
print(greetings)


# List comprehension with if else
"""
You have a list of prices of products in your online store
prices = [14.99, 13, 25, 9.99, 20, 34, 19.99]
if the price is greater than or equal to 20, apply a discount of 10%.
if the price is less than 20, increase the price by 10%.
"""
prices = [14.99, 13, 25, 9.99, 20, 34, 19.99]
new_prices = [price - price*(10/100) if price >= 20 else price + price*(10/100) for price in prices]
print(new_prices)
