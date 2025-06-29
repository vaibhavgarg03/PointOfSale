# Point of Sale System 
A simple and modular Point of Sale (PoS) system built in Python, designed to simulate the checkout process in a supermarket. It includes billing, offers, payment handling, and basic sales tracking.

## Features

1. **Calculate total bill** – Automatically sums prices for scanned items.
2. **Apply multibuy offers** – Adds discounts like "Three for the price of two" where applicable.
3. **Collect payment information** – Accepts and validates cash or card input.
4. **Print receipts (in £)** – Outputs a clear, itemized receipt in GBP.
5. **Store sales data** – Logs transactions for inventory and sales tracking.

## Installation

## Usage

## Modules
- [pointofsale.Card](#pointofsalecard): Handles the payment details when the payment method is Card. Stores the card number and the name on card entered by the user and verifies the format of the details.
- [pointofsale.Cash](#pointofsalecash): Handles the payment details when the payment method is Cash. Stores the amount entered by the user and checks it against the total amount on the bill.
- [pointofsale.Checkout](#pointofsalecheckout):  Handles the scanning of the items and calculation of the amount due before the customer is asked for payment details.
- [pointofsale.Item](#pointofsaleitem)
- [pointofsale.methods](#pointofsalemethods)
- [pointofsale.Receipt](#pointofsalereceipt)

<a name="pointofsalecard"></a>
## pointofsale.Card

Handles the payment details when the payment method is Card. Stores the card number and the name on card entered by the user and verifies the format of the details.

### Parameters
**`card_no`** : *int* or *str*  
16 digit numeric card number.

**`name_on_card`** : *str*  
Alphabetical, First name, Middle name (optional) and last name (optional) separated by a space.

### Attributes
**`pointofsale.Card.card_no`** : *str*  
16 digit numeric card number.

**`pointofsale.Card.name_on_card`** : *str*  
Alphabetical, First name, Middle name (optional) and last name (optional) separated by a space.

### Methods
**`pointofsale.Card.check_details(self)`** : *str*  
Verifies whether card number and name are valid.

**`pointofsale.Card._valid_card_number(self)`** : *bool*  
Checks whether the card number is numeric and exactly 16 digits.

**`pointofsale.Card._valid_name_format(self)`** : *bool*  
Checks whether the name on card is alphabetical and contains a first name, middle name (optional) and last name (optional) separated by a space.

## pointofsale.Cash

Handles the payment details when the payment method is Cash. Stores the amount entered by the user and checks it against the total amount on the bill.

### Parameters
**`amount_due`** : *int* <br>
Total amount due in pence.

**`amount_received`** : *int*  
Total amount received from customer in pence.

### Attributes
**`pointofsale.Cash.amount_due`** : *int* <br>
Total amount due in pence.

**`pointofsale.Cash.amount_received`** : *int*  
Total amount received from customer in pence.

### Methods
**`pointofsale.Cash.check_amount(self)`** : *str*  
Compares **`self.amount_due`** and **`self.amount_received`** to calculate change or balance.


## pointofsale.Checkout
Handles the scanning of the items and calculation of the amount due before the customer is asked for payment details.

### Parameters
**`prices`** : *dict* <br>
A dictionary of prices in pence. Example: {'A': 25, 'B': 40, 'P': 30}

### Attributes
**`pointofsale.Checkout.prices`** : *dict* <br>
A dictionary of prices in pence. Example: {'A': 25, 'B': 40, 'P': 30}

**`pointofsale.Checkout.scanned_items`** : *dict*  
A dictionary of scanned items and their count. Example: {'A': 2, 'B': 3, 'P': 1}

### Methods


## pointofsale.Item
## pointofsale.Receipt
## pointofsale.methods

## Data Files
### inventory.json
### sales.json

## Limitations

1. Since this is a PoS system, it doesn't take care of maintaining stocks or make changes to inventory. It only maintains sales data which can be fed to a stock management system. It also does not provide any way of changing the offer, however, that can easily be done by making changes to the "inventory.json" file.
2. If the payment method is card, only the name format and the card number is collected and verified. No additional data is collected (like card validity, account balance, etc), as in real world scenarios, a secure payment gateway would be required to do so.
3. Pence to Pound conversion happens only while printing the receipt, throughout the code there aren't any mechanisms to convert units. However, appropriate flags can be used to handle unit conversion in later versions.
4. Receipt is only printed to the console for now to reduce the unnecessary generation of metadata. However, the code can be modified to write the information to a file instead.