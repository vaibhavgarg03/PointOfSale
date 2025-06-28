import json
from Item import Item

class Checkout:
    def __init__(self, prices):
        """
        Initialize the Checkout with a dictionary of prices.
        Example: {'A': 25, 'B': 40, 'P': 30}
        """
        self.prices = prices
        self.scanned_items = {}

    def scan(self, item_code):
        """
        Register an item that has been scanned.
        """
        if item_code not in self.prices:
            raise ValueError(f"Unknown item code: {item_code}")
        self.scanned_items[item_code] = self.scanned_items.get(item_code, 0) + 1

    def total(self):
        """
        Calculate the total cost of all scanned items.
        """
        total = 0

        for item_code, quantity in self.scanned_items.items():
            price = self.prices[item_code]
            total += self.multi_buy(item_code, quantity, price).total

        return(total)
    
    def multi_buy(self, item_code, quantity, price):
        with open("inventory.json") as f:
            multi_buy_data = json.load(f)

        # Safety check in case item_code is missing in JSON
        item_data = multi_buy_data.get(item_code, {})

        item = Item(
            item_code=item_code,
            quantity=quantity,
            price=price,
            data=item_data
        )

        return item
        


        
    
    