# ───────────────────────────────────────────────────── Imports ────────────────────────────────────────────────────── #

# Standard Library
from typing import Union
# Third Party Library
# Private Library

# ────────────────────────────────────────────────────── Code ──────────────────────────────────────────────────────── #
""" 
NOTE:

1. We could use property decorator to get and set attribute values.
2. We could use pydantic to enforce validation constraints e.g., acnt must be 16 digits etc...
"""

class CreditCard:

    """A consumer credit card."""

    def __init__(self, customer: str, bank: str, acnt: int, limit: float):
        self.customer = customer
        self.bank = bank
        self.account = acnt
        self.limit = limit
        self.balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self.customer

    def get_bank(self):
        """Return the bank s name."""
        return self.bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self.account

    def get_limit(self):
        """Return current credit limit."""
        return self.limit

    def get_balance(self):
        """Return current balance."""
        return self.balance
    
    @staticmethod
    def _check_valid_number(val: Union[int, float]):
        """This function checks that the number passed via charge 
        or make payment is a valid number.

        Args:
            val (Union[int, float]): The value.
        """
        if not isinstance(val, (int, float)):
            raise ValueError('Value should be either int or float!')
        if val < 0:
            raise ValueError('Amount cannot be negative!')
        

    def charge(self, price: Union[int, float]) -> bool:
        """Charge given price to the card, assuming sufficient credit limit.

        Args:
            price (float): Price to charge.

        Returns:
            bool: Return True if charge was processed; False if charge was denied.
        """
        CreditCard._check_valid_number(val=price)
        # If charge exceeds limit
        if price + self.balance > self.limit:
            return False
        else:
            self.balance += price
        return True

    def make_payment(self, amount: Union[int, float]):
        """Process customer payment that reduces balance.

        Args:
            amount (float): The amount to reduce balance by.
        """
        CreditCard._check_valid_number(val=amount)
        self.balance -= amount

if __name__ == "__main__":
    cc = CreditCard(customer='Ben Dover',
                    bank='Halifax',
                    acnt='12345678',
                    limit=5000)
    print('Ben is making a purchase of £50!')
    cc.charge(50)
    print(f'Current balance: {cc.get_balance()}')
    print('Ben is repaying £25!')
    cc.make_payment(25)
    print(f'Current balance: {cc.get_balance()}')
