
# R-2.4) Write a Python class, Flower, that has three instance variables of type str, int, and float,
#   that respectively represent the name of the flower, its number of petals, and its price.
#   Your class must include a constructor method that initializes each variable to an appropriate value, and your class should
#   include methods for setting the value of each type, and retrieving the value of each type.

class Flower():
    def __init__(self, name: str, petal: int, price: float) -> None:
        self._name = name
        self._petal = petal
        self._price = price

    def get_name(self):
        """Returns the name of the flower
        """
        return self._name

    def get_petal(self):
        return self._petal

    def get_price(self):
        return self._price

    def set_name(self, name: str):
        self._name = name

    def set_petal(self, petal: int):
        self._petal = petal

    def set_price(self, price: float):
        self._price = price


# R-2.5) Use the techniques of Section 1.7 to revise the charge and make payment methods of the CreditCard class to ensure
#   that the caller sends a number as a parameter.
# R-2.6) If the parameter to the make payment method of the CreditCard class were a negative number,
#   that would have the effect of raising the balance on the account. Revise the implementation so that it raises a ValueError
#   if a negative value is sent.
# R-2.7) The CreditCard class of Section 2.3 initializes the balance of a new account to zero. Modify that class so that
#   a new account can be given a nonzero balance using an optional fifth parameter to the constructor. The four-parameter constructor syntax
#   should continue to produce an account with zero balance.
# R-2.8) Modify the declaration of the first for loop in the CreditCard tests, from Code Fragment 2.3, so that it will eventually cause exactly one of the three
#   credit cards to go over its credit limit. Which credit card is it?

# All questions solved by modifying th CreditCard class

class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer: str, bank: str, acnt: str, limit: float, balance=0) -> None:
        """Create a new credit card instance.

        The initial balance is zero

        Args:
            customer (str): name of the customer
            bank (str): name of the bank
            acnt (str): account identifier
            limit (float): credit limit
            balance(int): balance credit
        """
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        """Returns the name of the customer
        """
        return self._customer

    def get_bank(self):
        """Returns the name of the bank
        """
        return self._bank

    def get_account(self):
        """Returns the account number of the customer
        """
        return self._acnt

    def get_limit(self):
        """Returns current credit limit
        """
        return self._limit

    def get_balance(self):
        """Returns current balance
        """
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

            Return True if charge was processed; False if charge was denied.
        """
        if not isinstance(price, int):
            raise TypeError("Price must be an interger")

        if price + self._balance > self._limit:         # If charge exceeds limit cannot accept charge
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance.
        """
        if amount <= 0:
            raise ValueError(
                "Amount must be positive integer greater than zero")

        self._balance -= amount


if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard("John Bowman", "California Savings",
                  "5391 0375 9387 5309", 2500))
    wallet.append(CreditCard("John Bowman", "California Federal",
                  "3485 0399 3395 1954", 3500))
    wallet.append(CreditCard("John Bowman", "California Finance",
                  "5391 0375 9387 5309", 5000))

    # Changing 17 to 59 so that 3rd Credit card exceeds limit
    for val in range(1, 59):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print("Customer = ", wallet[c].get_customer())
        print("Bank = ", wallet[c].get_bank())
        print("Account = ", wallet[c].get_account())
        print("Limit = ", wallet[c].get_limit())
        print("Balance = ", wallet[c].get_balance())

        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New balance = ", wallet[c].get_balance())
        print()
