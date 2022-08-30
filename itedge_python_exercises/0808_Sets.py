"""
1) You have a set of customers for your online store.

customers = {'Alice', 'Bob', 'Carol', 'Dan'}

A new customer 'Ellen' has joined. Print the list of customers.
'Carol' has chosen to leave. Print the list of customers.

"""

customers = {'Alice', 'Bob', 'Carol', 'Dan'}
customers.add('Ellen')
print(f"The updated customer list:", customers)
customers.discard('Carol')
print(f"The updated customer list:", customers)


"""
2) Your company has a very strict dress code. Only certain color colothes can be worn in the office.

accepted_colors = {'white', 'black', 'grey'}

You have certain colors in your wardrobe.

my_colors = {'blue', 'red', 'black', 'green'}

What colors clothes can you wear.
Your company has added another color, "red" to their list. What options do u have now?
"""

accepted_colors = {'white', 'black', 'grey'}
my_colors = {'blue', 'red', 'black', 'green'}

wearable_colors = accepted_colors.intersection(my_colors)
print(f"Clothes color that I can wear to the company:", wearable_colors)

accepted_colors.add('red')
wearable_colors = accepted_colors.intersection(my_colors)
print(f"New clothes color that I can wear to the company:", wearable_colors)