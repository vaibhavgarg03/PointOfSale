# This class handles the scanning of the items and calculation of the amount due before the customer is asked for payment details.

__author__ = "Vaibhav Garg"
__email__ = "vaibhav.garg.0310@gmail.com"

# Import the relevant libraries
import json
from pointofsale.Item import Item


class Checkout:
    def __init__(self, prices):
        
        self.prices = prices # dict, a dictionary of prices in pence. Example: {'A': 25, 'B': 40, 'P': 30}
        self.scanned_items = {} # dict, a dictionary of scanned items and their count. Example: {'A': 2, 'B': 3, 'P': 1}

    def scan(self, item_code):
        
        # Registers an item that has been scanned.
        if item_code not in self.prices:
            # If the item code is not in the list of prices, raise an error
            raise ValueError(f"Unknown item code: {item_code}")
        
        self.scanned_items[item_code] = self.scanned_items.get(item_code, 0) + 1 # If the item code is in the list of prices, add 1 to the count

    def total(self):

        # returns: int, Calculates the total cost of all scanned items.
        total = 0

        for item_code, quantity in self.scanned_items.items():
            price = self.prices[item_code]
            total += self.item_details(item_code, quantity, price).total

        return(total)
    
    def item_details(self, item_code, quantity, price):

        # returns: object of class Item, Calculates the multibuy offer and the updated price
        with open("inventory.json") as f: # inventory.json is the path to the default data file. Can be changed according to user needs.
            multi_buy_data = json.load(f) # Accessing the inventory data

        # Safety check in case item_code is missing in JSON
        item_data = multi_buy_data.get(item_code, {})

        # Creating an instance of the Item class for a particular item
        item = Item(
            item_code=item_code,
            quantity=quantity,
            price=price,
            data=item_data
        )

        return item
        


        
    
    