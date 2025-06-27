import pytest
from Checkout import Checkout
from main import checkout

# Fixture for base prices
@pytest.fixture
def prices():
    return {'A': 25, 'B': 40, 'P': 30}

# Test individual item with no multibuy
def test_single_item(prices):
    assert checkout(['P'], prices) == 30  # Pear has no multibuy

# Test item A multibuy: 3 for 2 (3*25 normally = 75, with discount = 50)
def test_item_A_multibuy(prices):
    assert checkout(['A', 'A', 'A'], prices) == 50

# Test item B multibuy: 3 for 100
def test_item_B_multibuy(prices):
    assert checkout(['B', 'B', 'B'], prices) == 100

# Test mixed basket
def test_mixed_items(prices):
    assert checkout(['A', 'A', 'A', 'B', 'B', 'B', 'P'], prices) == 180
    # A x3 = 50, B x3 = 100, P = 30 → total = 180

# Test unscanned item raises error
def test_invalid_item_raises(prices):
    co = Checkout(prices)
    with pytest.raises(ValueError, match="Unknown item code: Z"):
        co.scan("Z")
