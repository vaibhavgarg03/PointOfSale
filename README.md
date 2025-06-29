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

---

**`pointofsale.Card._valid_card_number()`** : *bool* <br>
_This is a private/internal method._  
Checks whether the card number is numeric and exactly 16 digits.

#### Parameters
None

#### Returns

---

**`pointofsale.Card._valid_name_format()`** : *bool* <br>
_This is a private/internal method._  
Checks whether the name on card is alphabetical and contains a first name, middle name (optional) and last name (optional) separated by a space.

#### Parameters
None

#### Returns

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

**`item`**: *pointofsale.Item.Item*
Object containing details for an invidiual item including the multibuy offer and the updated price.

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