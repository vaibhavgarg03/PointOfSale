# Point of Sale System 
A simple and modular Point of Sale (PoS) system built in Python, designed to simulate the checkout process in a supermarket. It includes billing, offers, payment handling, and basic sales tracking.

## Features

1. **Calculate total bill** – Automatically sums prices for scanned items.
2. **Apply multibuy offers** – Adds discounts like "Three for the price of two" where applicable.
3. **Collect payment information** – Accepts and validates cash or card input.
4. **Print receipts (in £)** – Outputs a clear, itemized receipt in GBP.
5. **Store sales data** – Logs transactions for inventory and sales tracking.

## Installation

1. Clone the repository.

   ```bash
   https://github.com/vaibhavgarg03/PointOfSale.git
   ```

2. Navigate to the relevant directory and install using:
   ```bash
   pip install .
   ```

## Usage

### Using methods

1. Importing:
   ```python
   from pointofsale.methods import checkout, sales_data, print_receipt
   ```
2. Function calls:
   ```python
   items = ["A", "A", "A", "B", "B", "B", "P"]
   prices = {'A': 25, 'B': 40, 'P': 30}
   checkout(items, prices)
   ```
### Using Classes

1. Importing:
   ```python
   from pointofsale.Checkout import Checkout
   ```
2. Accessing attributes or methods:
   ```python
   prices = {'A': 25, 'B': 40, 'P': 30}
   check = Checkout(prices) #Initialise the prices
   item = {"A"}
   Checkout.scan(item)
   ```

**Note:** Please see `demo.py` and `demo_output.txt` for a more detailed demonstration.

## Modules
- [pointofsale.Card](#pointofsalecard): Handles the payment details when the payment method is Card. Stores the card number and the name on card entered by the user and verifies the format of the details.
- [pointofsale.Cash](#pointofsalecash): Handles the payment details when the payment method is Cash. Stores the amount entered by the user and checks it against the total amount on the bill.
- [pointofsale.Checkout](#pointofsalecheckout):  Handles the scanning of the items and calculation of the amount due before the customer is asked for payment details.
- [pointofsale.Item](#pointofsaleitem): Contains all the attributes related to a particular item. Also applies the multibuy offers based on the inventory data.
- [pointofsale.Receipt](#pointofsalereceipt): Contains all the attributes related to the purchase. Used to print the final receipt once the transaction is complete. Also takes care of printing error messages to the console and terminating the program.
- [pointofsale.methods](#pointofsalemethods): Contains essential methods to calculate the total costs, printing receipts and maintaining sales data.

<a name="pointofsalecard"></a>
## pointofsale.Card

Handles the payment details when the payment method is Card. Stores the card number and the name on card entered by the user and verifies the format of the details.

### Parameters
**`card_no`** : *int* or *str*  <br>
16 digit numeric card number.


**`name_on_card`** : *str*  <br>
Alphabetical, First name, Middle name (optional) and last name (optional) separated by a space.

---

### Attributes
**`pointofsale.Card.card_no`** : *str*  <br>
16 digit numeric card number.

**`pointofsale.Card.name_on_card`** : *str*  <br>
Alphabetical, First name, Middle name (optional) and last name (optional) separated by a space.

---

### Methods
**`pointofsale.Card.check_details()`** : *str*  <br>
Verifies whether card number and name are valid.

#### Parameters
None

#### Returns
Notifies whether card number and name are valid.

---

**`pointofsale.Card._valid_card_number()`** : *bool* <br>
_This is a private/internal method._  
Checks whether the card number is numeric and exactly 16 digits.

#### Parameters
None

#### Returns
Notifies whether the card number is numeric and exactly 16 digits.

---

**`pointofsale.Card._valid_name_format()`** : *bool* <br>
_This is a private/internal method._  
Checks whether the name on card is alphabetical and contains a first name, middle name (optional) and last name (optional) separated by a space.

#### Parameters
None

#### Returns
Notifies whether the name on card is alphabetical and contains a first name, middle name (optional) and last name (optional) separated by a space.

## pointofsale.Cash

Handles the payment details when the payment method is Cash. Stores the amount entered by the user and checks it against the total amount on the bill.

### Parameters
**`amount_due`** : *int* <br>
Total amount due in pence.

**`amount_received`** : *int*  <br>
Total amount received from customer in pence.

---

### Attributes
**`pointofsale.Cash.amount_due`** : *int* <br>
Total amount due in pence.

**`pointofsale.Cash.amount_received`** : *int*  <br>
Total amount received from customer in pence.

---

### Methods
**`pointofsale.Cash.check_amount()`** : *str*  <br>
Compares the amount due and the amount received to calculate change or balance.

#### Parameters
None

#### Returns
Returns calculated change, balance or notifies settled payment.

## pointofsale.Checkout
Handles the scanning of the items and calculation of the amount due before the customer is asked for payment details.

### Parameters
**`prices`** : *dict* <br>
A dictionary of prices in pence. Example: {'A': 25, 'B': 40, 'P': 30}

---

### Attributes
**`pointofsale.Checkout.prices`** : *dict* <br>
A dictionary of prices in pence. Example: {'A': 25, 'B': 40, 'P': 30}

**`pointofsale.Checkout.scanned_items`** : *dict*  <br>
A dictionary of scanned items and their count. Example: {'A': 2, 'B': 3, 'P': 1}

---

### Methods

**`pointofsale.Checkout.scan(item_code)`**: *None* <br>
Registers an item that has been scanned.

#### Parameters
**`item_code`**: *string* <br>
Item code for individual item. Example: "A" for Apple.

#### Returns

None

--- 

**`pointofsale.Checkout.total()`**: *int* <br>
Calculates the total cost of all scanned items.

#### Parameters
None

#### Returns
The total cost of all scanned items.

---

**`pointofsale.Checkout.item_details(item_code, quantity, price)`**: *pointofsale.Item.Item* <br>
Gathers details for an invidiual item including the multibuy offer and the updated price.

#### Parameters
**`item_code`**: *string* <br>
Item code for individual item. Example: "A" for Apple.

**`quantity`**: *int* <br>
Quantity of an individual item.

**`price`**: *int* <br>
Price in pence for an individual item.

#### Returns

**`item`**: *pointofsale.Item.Item* <br>
Object containing details for an invidiual item including the multibuy offer and the updated price.

## pointofsale.Item

Contains all the attributes related to a particular item. Also applies the multibuy offers based on the inventory data.

### Parameters

**`item_code`**: *string* <br>
Item code for individual item. Example: "A" for Apple.

**`quantity`**: *int* <br>
Quantity of an individual item.

**`price`**: *int* <br>
Price in pence for an individual item.

**`data`**: *Any* <br>
JSON Decoder object containing inventory data like item name, offer details, etc.

---

### Attributes
**`pointofsale.Item.item_code`**: *string* <br>
Item code for individual item. Example: "A" for Apple.

**`pointofsale.Item.name`**: *string* <br> 
Item name as provided in the inventory data. Example: "Apple".

**`pointofsale.Item.price`**: *int* <br> 
Price of the item in pence.

**`pointofsale.Item.quantity`**: *int* <br>
Quantity of the item.

**`pointofsale.Item.multi_buy_qty`**: *int* <br>
Quantity of item eligible for the offer.

**`pointofsale.Item.multi_buy_price`**: *int* or *None* <br>
If the multi buy offer has a fixed price, gets that price from inventory data. If the multi buy offer is a multiple of base price, gets the multiplier from inventory data and multiplies it with the base price. Returns None if there are no valid offers.

**`pointofsale.Item.total`**: *int* <br>
Stores the total cost of the identical items in pence.

**`pointofsale.Item.discount`**: *int* <br>
The discount that the customer received.

---

### Methods 

**`pointofsale.Item.calculate_total()`**: *int* <br>
Calculates the total cost of the identical items in pence after applying the offer.

#### Parameters

None

#### Returns

The total cost of the identical items in pence after applying the offer.

## pointofsale.Receipt

Contains all the attributes related to the purchase. Used to print the final receipt once the transaction is complete. Also takes care of printing error messages to the console and terminating the program.

### Parameters

**`items`**: *list* <br>
List of Item class objects. Contains details about all the items in the cart.

**`total_amount`**: *int* <br>
Total amount to be paid in pence.

**`payment_details`**: *dict* <br>
Payment details about the preferred payment method. Example: {"Cash": 100}

### Attributes

**`pointofsale.Receipt.datetime`**: *datetime* <br>
Gets the date and time from the console in DD/MM/YYYY HH:MM:SS format.

**`pointofsale.Receipt.items`**: *Any* <br>
Array of the Item class objects. Contains details about all the items in the cart.

**`pointofsale.Receipt.total_amount`**: *int* <br>
Total amount to be paid in pence.

**`pointofsale.Receipt.payment_details`**: *dict* <br>
Payment details about the preferred payment method. Example: {"Cash": 100}

### Methods

**`pointofsale.Receipt.add_payment_details()`**: *string* <br>
Gets payment details for the receipt or error messages to print to console.

#### Parameters
None

#### Returns
Payment details for the receipt or error messages to print to console.

---

**`pointofsale.Receipt.print_to_console()`**: *int* <br>
Checks for completion of transaction and prints the receipt or error messages to console.

#### Parameters
None

#### Returns
Notifies that the transaction was complete. 1 for yes, 0 for no.

## pointofsale.methods
Contains essential methods to calculate the total costs, printing receipts and maintaining sales data.

**`pointofsale.methods.checkout(item_codes, prices)`**: *int* <br>
Calculates the total cost of all items after applying the offers in pence.

### Parameters
**`item_codes`**: *list* <br>
Contains the item codes for the items scanned. Example: ["A","A","B","B","B","P"]

**`prices`**: *dict* <br>
Contains the item codes and prices for each item. Example: ["A": 25, "B": 40, "P": 30]

### Returns
Total cost of all the items after applying the offers in pence.

---

**`pointofsale.methods.print_receipt(item_codes, prices, payment_details)`**: *int* <br>
Prints the receipt and notifies whether or not the transaction was complete.

### Parameters
**`item_codes`**: *list* <br>
Contains the item codes for the items scanned. Example: ["A","A","B","B","B","P"]

**`prices`**: *dict* <br>
Contains the item codes and prices for each item. Example: ["A": 25, "B": 40, "P": 30]

**`payment_details`**: *dict* <br> 
Contains the payment details. Example: ["Cash": 100]

### Returns
Whether or not the transaction was complete: 1 for yes, 0 for no.

---

**`pointofsale.methods.sales_data(item_codes)`**: None <br>
Prints the sales data to a json file if the transaction was complete.

### Parameters
**`item_codes`**: *list* <br>
Contains the item codes for the items scanned. Example: ["A","A","B","B","B","P"]

### Returns
None

## Data Files
- `inventory.json`: Contains item metadata including name and optional multibuy offer rules.
- `sales.json`: Records the number of units sold per item code.

## Limitations

1. Since this is a PoS system, it doesn't take care of maintaining stocks or make changes to inventory. It only maintains sales data which can be fed to a stock management system. It also does not provide any way of changing the offer, however, that can easily be done by making changes to the "inventory.json" file.
2. If the payment method is card, only the name format and the card number is collected and verified. No additional data is collected (like card validity, account balance, etc), as in real world scenarios, a secure payment gateway would be required to do so.
3. Pence to Pound conversion happens only while printing the receipt, throughout the code there aren't any mechanisms to convert units. However, appropriate flags can be used to handle unit conversion in later versions.
4. Receipt is only printed to the console for now to reduce the unnecessary generation of metadata. However, the code can be modified to write the information to a file instead.