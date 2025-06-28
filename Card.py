class Card:
    def __init__(self, card_no, name_on_card):
        self.card_no = str(card_no)
        self.name_on_card = name_on_card

    def check_details(self):
        if self._valid_card_number() and self._valid_name_format():
            masked = "**** **** **** " + self.card_no[-4:]
            return f"Paid by Card: {masked}\nName on Card: {self.name_on_card}"
        
        else:
            return "Invalid Card"

    def _valid_card_number(self):
        return self.card_no.isdigit() and len(self.card_no) == 16

    def _valid_name_format(self):
        # Match: First [Middle] Last (2 or 3 words), all alphabetic
        name_parts = self.name_on_card.strip().split()
        if len(name_parts) not in [1, 2, 3]:
            return False
        return all(part.isalpha() for part in name_parts)