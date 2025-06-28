from Checkout import Checkout
from Card import Card
from Cash import Cash
from Receipt import Receipt

def checkout (item_codes, prices):

    check = Checkout(prices)
    for item in item_codes:
        check.scan(item)
    return(check.total())

def print_receipt(item_codes, prices, payment_details):

    check = Checkout(prices)
    for item in item_codes:
        check.scan(item)

    items = {}
    for item_code, quantity in check.scanned_items.items():
        items[item_code] = check.multi_buy(item_code, quantity, prices[item_code])

    receipt = Receipt(items, check.total(), payment_details)
    receipt.print_to_console()

print_receipt(['A', 'A', 'A', 'B', 'B', 'B', 'P'], {'A': 25, 'B': 40, 'P': 30}, {"Cash": 100})