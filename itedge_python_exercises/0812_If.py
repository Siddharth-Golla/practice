"""
Define two variables.

has_eggs = True
has_bacon = False

A man goes to the market.His instructions are:
If you find eggs, buy 12
If you buy eggs and you also find bacon, buy two packs
Egg cost 5 each.A pack of bacon costs 20. How much does the man spend at the market?

"""

has_eggs = True
has_bacon = False
expenditure = 0

if has_eggs:
    expenditure = expenditure + (12*5)
    if has_bacon:
        expenditure = expenditure + (20*2)


print(f"The man spends {expenditure}.")