# This code tests the print_receipt method (and in turn payment verification and item details process) from methods.py

__author__ = "Vaibhav Garg"
__email__ = "vaibhav.garg.0310@gmail.com"

# Import the relevant libraries
import pytest
from pointofsale.methods import print_receipt

# Sample data 
item_codes = ['A', 'A', 'A', 'B', 'B', 'B', 'P']
prices = {'A': 25, 'B': 40, 'P': 30}


# Fixtures for different payment methods
@pytest.fixture
def valid_card():
    return {"Card": [1234567890123456, "Vaibhav Garg"]} # Valid card

@pytest.fixture
def invalid_card_no():
    return {"Card": [12345678901, "Vaibhav Garg"]} # Invalid Card Number

@pytest.fixture
def invalid_name():
    return {"Card": [1234567890123456, "Vaibhav123"]} # Invalid Name on card (Alphanumeric)

@pytest.fixture
def invalid_name2():
    return {"Card": [1234567890123456, "Vaibhav G A Rg"]} # Invalid Name on card (Too long)

@pytest.fixture
def exact_cash():
    return {"Cash": 180}  # Total is 180 (in pence)

@pytest.fixture
def excess_cash():
    return {"Cash": 300}  # Will require confirmation: change

@pytest.fixture
def short_cash():
    return {"Cash": 100}  # Will require confirmation: balance


# Tests
def test_receipt_with_valid_card(capfd, valid_card):
    # Test receipt generation with a valid card
    print_receipt(item_codes, prices, valid_card)
    out, _ = capfd.readouterr()
    assert "Paid by Card" in out
    assert "Vaibhav Garg" in out
    assert "Item Code" in out
    assert "Total:" in out

def test_receipt_with_invalid_card_no(capfd, invalid_card_no):
    # Test receipt generation with an invalid card number
    print_receipt(item_codes, prices, invalid_card_no)
    out, _ = capfd.readouterr()
    assert "Invalid Card" in out
    assert "Transaction failed!" in out

def test_receipt_with_invalid_name(capfd, invalid_name):
    # Test receipt generation with invalid name (alphanumeric name)
    print_receipt(item_codes, prices, invalid_name)
    out, _ = capfd.readouterr()
    assert "Invalid Card" in out
    assert "Transaction failed!" in out

def test_receipt_with_invalid_name2(capfd, invalid_name2):
    # Test receipt generation with invalid name (more than three parts)
    print_receipt(item_codes, prices, invalid_name2)
    out, _ = capfd.readouterr()
    assert "Invalid Card" in out
    assert "Transaction failed!" in out

def test_receipt_with_exact_cash(capfd, exact_cash):
    # Test receipt generation with exact cash
    # No input required if cash matches exactly
    print_receipt(item_codes, prices, exact_cash)
    out, _ = capfd.readouterr()
    assert "Paid with Cash" in out
    assert "Total:" in out

def test_receipt_with_change_confirmed(capfd, excess_cash, monkeypatch):
    # Test receipt generation with change received confirmation
    monkeypatch.setattr("builtins.input", lambda _: "y") # Mimics input from user
    print_receipt(item_codes, prices, excess_cash)
    out, _ = capfd.readouterr()
    assert "Change (£)" in out
    assert "Total:" in out


def test_receipt_with_change_declined(capfd, excess_cash, monkeypatch):
    # Test receipt generation when change is not received
    monkeypatch.setattr("builtins.input", lambda _: "n") # Mimics input from user
    print_receipt(item_codes, prices, excess_cash)
    out, _ = capfd.readouterr()
    assert "Transaction failed" in out


def test_receipt_with_balance_confirmed(capfd, short_cash, monkeypatch):
    # Test receipt generation with balance paid confirmation
    monkeypatch.setattr("builtins.input", lambda _: "y") # Mimics input from user
    print_receipt(item_codes, prices, short_cash)
    out, _ = capfd.readouterr()
    assert "Balance (£)" in out
    assert "Total:" in out


def test_receipt_with_balance_declined(capfd, short_cash, monkeypatch):
    # Test receipt generation when balance was not paid
    monkeypatch.setattr("builtins.input", lambda _: "n") # Mimics input from user
    print_receipt(item_codes, prices, short_cash)
    out, _ = capfd.readouterr()
    assert "Transaction failed" in out
