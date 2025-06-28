from Card import Card
from Cash import Cash
from datetime import datetime

class Receipt:
    def __init__(self, items, total_amount, payment_details):
        self.datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.items = items
        self.total_amount = total_amount
        self.payment_details = payment_details

    def add_payment_details(self):
        if 'Card' in self.payment_details:
            card = Card(*self.payment_details["Card"])
            return card.check_details()

        elif 'Cash' in self.payment_details:
            cash = Cash(self.total_amount, self.payment_details["Cash"])
            return cash.check_amount()
    
    def print_to_console(self):
        result = self.add_payment_details()  # Call it once and store result

        if result == "Invalid Card":
            print(result)
            print("Transaction failed! Please try again.")
            return

        elif 'Cash' in self.payment_details and result != "Paid with Cash":
            print(result)
            confirmation = input("Did you " + ("receive the change? " if "change" in result.lower() else "pay the balance? ") + "(y/n): ").strip().lower()

            if confirmation != 'y':
                print("Transaction failed! Please try again.")
                return
            else:
                result = "Paid with Cash"
    
        print(self.datetime)
        print("-" * 70)
        print("-" * 70)
        print(f"{'Item Code':<20}{'Name':<25}{'Quantity':<15}{'Price (£)':<10}")
        print(f"{'':<56}{'Discount  (£)':>10}")
    
        for item in self.items.values():
            # Assume .total and .discount already exist
            print(f"{item.item_code:<20}{item.name:<25}{item.quantity:<15}{(item.quantity*item.price)/100:<10}")
            print(f"{'':<60}{-item.discount/100:>10.2f}")

        print("-" * 70)
        print(f"{'Total:':<58}£{self.total_amount / 100:>5.2f}")
        print("-" * 70)
        print(f"{result}")

        