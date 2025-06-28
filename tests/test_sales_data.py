import json
import pytest
from pointofsale.methods import sales_data  # Adjust the import path if needed
import os

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

def test_sales_data_update():
    sales_data(['A', 'A', 'B', 'P'])
    
    with open("sales.json") as f:
        updated = json.load(f)
    
    expected = {"A": 4, "B": 2, "P": 3}
    assert updated == expected

