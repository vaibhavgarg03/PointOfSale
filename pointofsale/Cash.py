# This class handles the payment details when the payment method is Cash. It stores the amount entered by the user and checks it against the total amount on the bill.

__author__ = "Vaibhav Garg"
__email__ = "vaibhav.garg.0310@gmail.com"

class Cash:
    def __init__(self, amount_due, amount_received):
        self.amount_due = amount_due # int, total amount due in pence
        self.amount_received = amount_received # int, total amount received from user in pence

    def check_amount(self):
        # returns: string, Compares self.amount_due and self.amount_received to calculate change or balance
        if self.amount_due > self.amount_received:
            # If self.amount_due > self.amount_received, ask for the balance amount
            balance = self.amount_due - self.amount_received 
            return f"Balance (£): {balance/100}"
        
        elif self.amount_due < self.amount_received:
            # If self.amount_due < self.amount_received, return the change
            change = self.amount_received - self.amount_due
            return f"Change (£): {change/100}"
        
        else:
            # If self.amount_due = self.amount_received, notify that the payment was completed with cash
            return f"Paid with Cash" 