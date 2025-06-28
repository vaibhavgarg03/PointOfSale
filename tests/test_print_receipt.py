import pytest
from pointofsale.methods import print_receipt

# --- Sample data ---
item_codes = ['A', 'A', 'A', 'B', 'B', 'B', 'P']
prices = {'A': 25, 'B': 40, 'P': 30}


# --- Fixtures for different payment methods ---
@pytest.fixture
def valid_card():
    return {"Card": [1234567890123456, "Vaibhav Garg"]}

@pytest.fixture
def invalid_card_no():
    return {"Card": [12345678901, "Vaibhav Garg"]}

@pytest.fixture
def invalid_name():
    return {"Card": [1234567890123456, "Vaibhav123"]}

@pytest.fixture
def exact_cash():
    return {"Cash": 180}  # Total is 180 (in pence)

@pytest.fixture
def excess_cash():
    return {"Cash": 300}  # Will require confirmation: change

@pytest.fixture
def short_cash():
    return {"Cash": 100}  # Will require confirmation: balance


# --- Tests ---
def test_receipt_with_valid_card(capfd, valid_card):
    print_receipt(item_codes, prices, valid_card)
    out, _ = capfd.readouterr()
    assert "Paid by Card" in out
    assert "Vaibhav Garg" in out
    assert "Item Code" in out
    assert "Total:" in out

def test_receipt_with_invalid_card_no(capfd, invalid_card_no):
    print_receipt(item_codes, prices, invalid_card_no)
    out, _ = capfd.readouterr()
    assert "Invalid Card" in out
    assert "Transaction failed!" in out

def test_receipt_with_invalid_name(capfd, invalid_name):
    print_receipt(item_codes, prices, invalid_name)
    out, _ = capfd.readouterr()
    assert "Invalid Card" in out
    assert "Transaction failed!" in out

def test_receipt_with_exact_cash(capfd, exact_cash):
    # No input required if cash matches exactly
    print_receipt(item_codes, prices, exact_cash)
    out, _ = capfd.readouterr()
    assert "Paid with Cash" in out
    assert "Total:" in out

def test_receipt_with_change_confirmed(capfd, excess_cash, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    print_receipt(item_codes, prices, excess_cash)
    out, _ = capfd.readouterr()
    assert "Change (£)" in out
    assert "Total:" in out


def test_receipt_with_change_declined(capfd, excess_cash, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    print_receipt(item_codes, prices, excess_cash)
    out, _ = capfd.readouterr()
    assert "Transaction failed" in out


def test_receipt_with_balance_confirmed(capfd, short_cash, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    print_receipt(item_codes, prices, short_cash)
    out, _ = capfd.readouterr()
    assert "Balance (£)" in out
    assert "Total:" in out


def test_receipt_with_balance_declined(capfd, short_cash, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    print_receipt(item_codes, prices, short_cash)
    out, _ = capfd.readouterr()
    assert "Transaction failed" in out
