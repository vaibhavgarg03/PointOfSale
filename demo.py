# This is a demonstration of how the code can be used to implement a basic Point of Sale (PoS) system.
# It is designed from the perspective of an average user, focusing on typical usage scenarios.
# As such, the demo does not include rigorous error handling, in order to simulate how a less experienced user might interact with the system.
# However, the underlying package is designed to handle errors gracefully and manage unexpected inputs during actual operation.
# Note: See demo_output.txt for examples.

__author__ = "Vaibhav Garg"
__email__ = "vaibhav.garg.0310@gmail.com"

# Import the relevant methods
from pointofsale.methods import checkout, sales_data, print_receipt

# Initialize an empty list to hold scanned items
items = []

# Set base prices (to be done within the code, not via console)
prices = {'A': 25, 'B': 40, 'P': 30}

# Flag to check if transaction completes
transaction = 0

# Add instructions to the console
print("WELCOME!")
print("Scan your items one at a time.")
print("Enter '1' to proceed to payment.")


while True:
    # Scan items until user enters 1.
    item = input("Scan item (or enter 1 to pay): ")
    if item.strip() == "1":
        break
    items.append(item.strip().upper())
    print(f"Total (£): {checkout(items, prices)/100}") # Display the total amount as the items are scanned.

# Take payment details if the cart is not empty
if items != []:
    payment_method = input("How would you like to pay (Cash/Card): ").title()
else:
    print("Empty cart. Exiting...")
    exit(0)

if payment_method == "Cash":
    # Handle cash payment
    amount = float(input("Enter the amount being paid (£): "))
    payment_details = {"Cash": amount*100}

elif payment_method == "Card":
    # Handle card payment
    card_no = int(input("Enter the card number: "))
    name_on_card = input("Enter the name on card: ").title()
    payment_details = {"Card": [card_no, name_on_card]}

else:
    # Handle invalid input
    print("Unsupported payment method.")

# Print receipt and check if the transaction is complete
transaction = print_receipt(items, prices, payment_details)

# Update the sales data if transaction was complete
if transaction == 1:
    sales_data(items)
    print("Thanks for shopping!")
else:
    print("Exiting...")