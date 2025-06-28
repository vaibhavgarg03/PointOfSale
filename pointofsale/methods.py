import json
from collections import Counter
from pointofsale.Checkout import Checkout
from pointofsale.Receipt import Receipt

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

def sales_data(item_codes):
    try:
        with open("sales.json", "r") as f:
            existing = Counter(json.load(f))
    except FileNotFoundError:
        existing = Counter()

    updated = existing + Counter(item_codes)

    with open("sales.json", "w") as f:
        json.dump(updated, f, indent=2)
