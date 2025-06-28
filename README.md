# Point Of Sale (PoS) System
Competency test for the Research Software Engineer role at Imperial College London.

## Features

1. Calculate total costs
2. Apply offers
3. Collect payment information
4. Print receipts (in £)
5. Store sales data for inventory management

## Classes

### Checkout.py
### Item.py 

## Data File
inventory.json

## Limitations

1. Since this is a PoS system, it doesn't take care of maintaining stocks or make changes to inventory. It only maintains sales data which can be fed to a stock management system.
2. If the payment method is card, only the name format and the card number is collected and verified. No additional data is collected (like card validity, account balance, etc), as in real world scenarios, a secure payment gateway would be required to do so.