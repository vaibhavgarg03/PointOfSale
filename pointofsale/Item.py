# This class contains all the attributes related to a particular item. It also applies the multibuy offers based on the inventory data.

__author__ = "Vaibhav Garg"
__email__ = "vaibhav.garg.0310@gmail.com"

class Item:
    def __init__(self, item_code, quantity, price, data):
        
        self.item_code = item_code # string, Item code for a particular item
        self.name = data.get("item_name", item_code) # string, Item name as provided in the inventory data
        self.price = price # int, price of the item in pence
        self.quantity = quantity # int, quantity of the item
        self.multi_buy_qty = data.get("multi_buy_qty") # int, the quantity of item eligible for the offer

        if "multi_buy_price" in data:
            # If the multi buy offer has a fixed price, get that price from inventory data
            self.multi_buy_price = data["multi_buy_price"] # int, the price in pence
        elif "multiplier" in data and self.multi_buy_qty:
            # If the multi buy offer is a multiple of base price, get the multiplier from inventory data
            self.multi_buy_price = data["multiplier"] * price # int, the price of a single item times the multiplier
        else:
            # return None if there are no valid offers
            self.multi_buy_price = None

        self.total = self.calculate_total() # int, stores the total cost of the identical items in pence
        self.discount = self.price * self.quantity - self.total # int, the discount that the customer received

    def calculate_total(self):
        # returns: int, calculates the total cost of the identical items in pence after applying the offer

        if self.multi_buy_qty and self.multi_buy_price:
            # If the multibuy offer exists, apply the discounted price for the grouped items, and the regular price for the remaining items
            groups = self.quantity // self.multi_buy_qty
            remainder = self.quantity % self.multi_buy_qty
            return groups * self.multi_buy_price + remainder * self.price
        else:
            # If the multibuy offer does not exist, apply the regular price for the items
            return self.quantity * self.price