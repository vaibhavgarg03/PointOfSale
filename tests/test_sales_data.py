# This code tests the sales_data method from methods.py.

__author__ = "Vaibhav Garg"
__email__ = "vaibhav.garg.0310@gmail.com"

# Import the relevant libraries
import json
import pytest
from pointofsale.methods import sales_data
import os

# Fixture to setup and cleanup sales.json for each test
@pytest.fixture(autouse=True)
def setup_and_cleanup():
    # Setup: create initial sales.json before each test
    initial = {"A": 2, "B": 1, "P": 2}
    with open("sales.json", "w") as f:
        json.dump(initial, f)
    
    yield  # Run the test
    
    # Cleanup: remove sales.json after each test
    if os.path.exists("sales.json"):
        os.remove("sales.json")

# Test if sales_data correctly updates the sales.json file
def test_sales_data_update():
    sales_data(['A', 'A', 'B', 'P'])
    
    with open("sales.json") as f:
        updated = json.load(f)
    
    expected = {"A": 4, "B": 2, "P": 3}
    assert updated == expected

# Test if sales_data creates a new sales.json file
def test_sales_data_creates_new_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)  # Switch to a clean temp directory
    assert not os.path.exists("sales.json")  # Confirm it doesn't exist

    sales_data(['A', 'B', 'P'])  # Run function (should hit except block)

    with open("sales.json") as f:
        updated = json.load(f)

    expected = {"A": 1, "B": 1, "P": 1}
    assert updated == expected