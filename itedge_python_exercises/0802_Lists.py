"""
1) You have a list of objects on your desk => laptop, mouse, pen, paper, mug, phone.
Print out the third element.
Print out the first 3 elements.
Print out all the elements except the first 2.

"""
objects = ["laptop", "mouse", "pen", "paper", "mug", "phone"]
print(f"The third element in the list is {objects[2]}.")
print(f"The first three elements are {objects[:3]}")
print(f"All elements except the first 2 : {objects[2:]}")


"""
2) A zoo has a list of animals

animals = ['lion', 'zebra', 'chimp', 'elephant']

A new panda has arrived. Print out the new list of animals.

The lion has been given to a different zoo. Print out the new list of animals.

Does the zoo have an elephant? How about a giraffe?
"""

animals = ['lion', 'zebra', 'chimp', 'elephant']
animals.append('panda')
print(f"The updated list of animals after adding panda:", animals)
animals.remove('lion')
print(f"The updated list of animals after removing lion:", animals)