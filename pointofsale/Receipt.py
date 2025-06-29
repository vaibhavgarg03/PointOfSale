# This class contains all the attributes related to the purchase. It is used to print the final receipt once the transaction is complete. It also takes care
# of printing error messages to the console and terminating the program.

__author__ = "Vaibhav Garg"
__email__ = "vaibhav.garg.0310@gmail.com"

# Import the relevant libraries
from pointofsale.Card import Card
from pointofsale.Cash import Cash
from datetime import datetime

class Receipt:
    def __init__(self, items, total_amount, payment_details):
        self.datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # datetime object, gets the date and time from the console in DD/MM/YYYY HH:MM:SS format
        self.items = items # an array of the Item class objects, contains details about all the items in the cart
        self.total_amount = total_amount # int, total amount to be paid in pence
        self.payment_details = payment_details # dict, payment details about the preferred payment method. Example: {"Cash": 100}

    def add_payment_details(self):
        # returns: string, gets payment details for the receipt or error messages to print to console
        if 'Card' in self.payment_details:
            card = Card(*self.payment_details["Card"]) # Creating an instance of the Card class
            return card.check_details() # Verifying card details

        elif 'Cash' in self.payment_details:
            cash = Cash(self.total_amount, self.payment_details["Cash"]) # Creating an instance of the Cash class
            return cash.check_amount() # Checking the received amount
    
    def print_to_console(self):
        # returns: int, checks for completion of transaction and prints the receipt or error messages to console
        result = self.add_payment_details()  # Call it once and store result

        if result == "Invalid Card":
            # If the card details are invalid, terminate the process and ask the customer to try again. Prints the error messages.
            print(result)
            print("Transaction failed! Please try again.")
            return 0

        elif 'Cash' in self.payment_details and result != "Paid with Cash":
            # If the cash paid is over or under the required amount, ask the customer if they cleared the balance or received change. If yes, print receipt.
            # If not, terminate the process and ask the customer to try again. Prints the error messages.
            print(result)
            confirmation = input("Did you " + ("receive the change? " if "change" in result.lower() else "pay the balance? ") + "(y/n): ").strip().lower()

            if confirmation != 'y':
                print("Transaction failed! Please try again.")
                return 0
            else:
                result = "Paid with Cash"
    
        print(self.datetime) # Prints the date on top
        print("-" * 70) # Adds a horizontal line on the receipt
        print("-" * 70) # Adds another horizontal line on the receipt
        print(f"{'Item Code':<20}{'Name':<25}{'Quantity':<15}{'Price (£)':<10}") # Prints the column names on the receipt 
        print(f"{'':<56}{'Discount  (£)':>10}")                                  # and adjusts them properly
    
        for item in self.items.values():
            # Prints the item details on the receipt and adjusts them in appropriate columns
            print(f"{item.item_code:<20}{item.name:<25}{item.quantity:<15}{(item.quantity*item.price)/100:<10}")
            print(f"{'':<60}{-item.discount/100:>10.2f}")

        print("-" * 70) # Adds another horizontal line on the receipt
        print(f"{'Total:':<58}£{self.total_amount / 100:>5.2f}") # Print the total amount on the receipt in £
        print("-" * 70) # Adds another horizontal line on the receipt
        print(f"{result}") # Prints the payment details on the receipt
        return 1 # Notifies that the transaction was complete

        