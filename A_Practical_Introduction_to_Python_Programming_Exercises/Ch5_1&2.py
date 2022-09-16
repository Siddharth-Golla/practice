"""
1) Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 1.
"""
end_with_1 = 0
for i in range(1,101):
    if i*i % 10 == 1:
        end_with_1 = end_with_1 + 1
print(f"The number of squares of the numbers from 1 to 100 ending with 1 is", end_with_1)


"""
2) Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
4 and how many end in a 9.
"""

end_with_4 = 0
end_with_9 = 0
for i in range(1, 101):
    if i * i % 10 == 4:
        end_with_4 = end_with_4 + 1
    if i * i % 10 == 9:
        end_with_9 = end_with_9 + 1
print(f"The number of squares of the numbers from 1 to 100 ending with 4 is", end_with_4, "and ending with 9 is", end_with_9)

