"""Read from the console the amount the user has in their bank account.
The interest on that account is 5.5% per year.
How much would that user have in 5 years?
"""

amount = input("Enter your amount: ")
interest_5_years = ((5.5/100) * float(amount)) * 5
amount_5_years = float(amount) + interest_5_years
print(f"In 5 years the user will have {amount_5_years} Rs.")
