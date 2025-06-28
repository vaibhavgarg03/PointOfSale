class Cash:
    def __init__(self, amount_due,amount_received):
        self.amount_due = amount_due
        self.amount_received = amount_received

    def check_amount(self):
        if self.amount_due > self.amount_received:
            balance = self.amount_due - self.amount_received
            return f"Balance (£): {balance/100}"
        elif self.amount_due < self.amount_received:
            change = self.amount_received - self.amount_due
            return f"Change (£): {change/100}"
        else:
            return f"Paid with Cash" 