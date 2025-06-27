class Item:
    def __init__(self, item_code, quantity, price, data):
        """
        :param item_code: string, e.g., "A"
        :param price: int, base price for a single unit
        :param data: dict, from JSON, e.g., {
            "item_name": "Apple",
            "multi_buy_qty": 3,
            "multiplier": 2
        }
        """
        self.item_code = item_code
        self.name = data.get("item_name", item_code)
        self.price = price
        self.quantity = quantity
        self.multi_buy_qty = data.get("multi_buy_qty")

        if "multi_buy_price" in data:
            self.multi_buy_price = data["multi_buy_price"]
        elif "multiplier" in data and self.multi_buy_qty:
            self.multi_buy_price = data["multiplier"] * price
        else:
            self.multi_buy_price = None

    def calculate_total(self):
        if self.multi_buy_qty and self.multi_buy_price:
            groups = self.quantity // self.multi_buy_qty
            remainder = self.quantity % self.multi_buy_qty
            return groups * self.multi_buy_price + remainder * self.price
        else:
            return self.quantity * self.price