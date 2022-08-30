# C-2.28) The PredatoryCreditCard class of Section 2.4.1 provides a process_month method that models the completion of a monthly cycle.
#   Modify the class so that once a customer has made ten calls to charge in the current month, each additional call to that function
#   results in an additional $1 surcharge

# C-2.29) Modify the PredatoryCreditCard class from Section 2.4.1 so that a customer is assigned a minimum monthly payment,
#   as a percentage of the balance, and so that a late fee is assessed if the customer does not subsequently pay that minimum amount
#   before the next monthly cycle.

# C-2.30) At the close of Section 2.4.1, we suggest a model in which the CreditCard class supports a nonpublic method, _set_balance(b),
#   that could be used by subclasses to affect a change to the balance, without directly accessing the _balance data member.
#   Implement such a model, revising both the CreditCard and PredatoryCreditCard classes accordingly.

# All solutions completed by revising the CreditCard and PredatoryCreditCard classes.

from Chp2_R4_R8 import CreditCard


class PredatoryCreditClass(CreditCard):
    """An extension to CreditCard that compounds interest and fee."""

    def __init__(self, customer: str, bank: str, acnt: str, limit: float, balance, apr) -> None:
        """Create a new predatory credit card instance.

        customer    the name of the customer (e.g., "John Bowman")
        bank        the name of the bank (e.g., "California Savings")
        acnt        the acount identifier (e.g., "5391 0375 9387 5309")
        limit       credit limit (measured in dollars)
        apr         annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit, balance)
        self._apr = apr
        self._charge_count = 0

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Args:
            price (int): Price to be charged

        Returns:
            bool    : Return True if charge was processed; otherwise False and assess 5$ fee
        """
        success = super().charge(price)                             # Call to inherited method
        self._charge_count += 1
        # Check if number of charges is more than 10 in a month
        if self._charge_count > 10:
            self._balance += 1                                      # Asses 1$ surcharge
        if not success:
            # Asses the 5$ fee if not successful
            self._balance += 5
        # caller expects return value
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance."""

        # Reset the charge count to zero every monthly cycle
        self._charge_count = 0

        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
