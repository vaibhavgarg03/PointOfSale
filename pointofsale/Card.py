# This class handles the payment details when the payment method is Card. It stores the card number and the name on card entered by the user and verifies the format 
# of the details.

__author__ = "Vaibhav Garg"
__email__ = "vaibhav.garg.0310@gmail.com"

class Card:
    def __init__(self, card_no, name_on_card):
        self.card_no = str(card_no) # string, 16 digit numeric card number
        self.name_on_card = name_on_card.title() # string, alphabetical, first name, middle name (optional) and last name separated by a space

    def check_details(self):
        # returns: string, Verifies whether card number and name are valid
        if self._valid_card_number() and self._valid_name_format():
            # If the details provided are valid, returns the masked card number and name to be printed on the receipt
            masked = "**** **** **** " + self.card_no[-4:]
            return f"Paid by Card: {masked}\nName on Card: {self.name_on_card}"
        
        else:
            # If the details provided are invalid, notifies the user and terminates the transaction
            return "Invalid Card"

    def _valid_card_number(self):
        # returns: boolean, Checks whether the card number is numeric and exactly 16 digits
        return self.card_no.isdigit() and len(self.card_no) == 16

    def _valid_name_format(self):
        # returns: boolean, Checks whether the name on card is alphabetical and contains a first name, middle name (optional) and last name (optional) 
        # separated by a space
        name_parts = self.name_on_card.strip().split()
        if len(name_parts) not in [1, 2, 3]:
            return False
        return all(part.isalpha() for part in name_parts)