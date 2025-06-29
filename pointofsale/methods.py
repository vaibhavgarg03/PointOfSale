# This file contains essential methods to calculate the total costs, printing receipts and maintaining sales data.

__author__ = "Vaibhav Garg"
__email__ = "vaibhav.garg.0310@gmail.com"

# Import the relevant libraries and classes
import json
from collections import Counter
from pointofsale.Checkout import Checkout
from pointofsale.Receipt import Receipt

def checkout (item_codes, prices):
    # Calculates the total cost of all items after applying the offers in pence
    # params: item_codes: list of strings, contains the item codes for the items scanned. Example: ["A","A","B","B","B","P"]
    #         prices: dict, contains the item codes and prices for each item. Example: ["A": 25, "B": 40, "P": 30]
    # returns: int, total cost of all the items after applying the offers in pence
    check = Checkout(prices) #Initialise the prices
    for item in item_codes:
        check.scan(item) # Scan the items
    return(check.total()) # Return the total cost

def print_receipt(item_codes, prices, payment_details):
    # Prints the receipt and notifies whether or not the transaction was complete.
    # params: item_codes: list of strings, contains the item codes for the items scanned. Example: ["A","A","B","B","B","P"]
    #         prices: dict, contains the item codes and prices for each item. Example: ["A": 25, "B": 40, "P": 30]
    #         payment_details: dict, contains the payment details. Example: ["Cash": 100]
    # returns: int, 1 if the transaction was complete, 0 if not

    check = Checkout(prices) #Initialise the prices
    for item in item_codes:
        check.scan(item) # Scan the items

    items = {} # Empty dictionary to assign item class objects to unique item codes
    for item_code, quantity in check.scanned_items.items():
        items[item_code] = check.item_details(item_code, quantity, prices[item_code]) # Gather item details for unique item codes

    receipt = Receipt(items, check.total(), payment_details) # Verify payment process and print receipt
    return receipt.print_to_console() # Notifies whether or not the transaction was complete: 1 for yes, 0 for no.

def sales_data(item_codes):
    # Prints the sales data to a json file if the transaction was complete.
    # params: item_codes: list of strings, contains the item codes for the items scanned. Example: ["A","A","B","B","B","P"]
    
    try:
        # Try to read existing sales data from sales.json
        with open("sales.json", "r") as f:
            existing = Counter(json.load(f))
    except FileNotFoundError:
        # If file doesn't exist, start with an empty counter
        existing = Counter()

    # Count new items and add them to existing sales data
    updated = existing + Counter(item_codes)

    # Write the updated sales data back to sales.json
    with open("sales.json", "w") as f:
        json.dump(updated, f, indent=2)
