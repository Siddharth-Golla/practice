"""
1) A network server has sent you the following tuple, which contains the web address, protocol and port

Contruct the web address with following format, print it to the console

<protocol>://www.<address>:<port>

"""

connection = ('google.com', 'https', 80)

print(connection[1], '://www.', connection[0], ':', str(connection[2]), sep='')





"""
2) You have a tuple of some prime numbers

primes = (2, 3, 5, 7, 11, 13)

Print out the size of the tuple.
Which index is the number 11?
Add the following prime numbers and print out the resulting tuple

new_primes = (17, 19, 23)
"""

primes = (2, 3, 5, 7, 11, 13)
print(f"The size of the tuple: ", len(primes))
print(f"The index of the value 11:", primes.index(11))

new_primes = primes[:] + (17,19,23)
print(f"The new resulting tuple:", new_primes)