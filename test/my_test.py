
# test/my_test.py

from app.shopping_cart import to_usd

def test_to_usd():
    result = to_usd(5)
    assert result == "$5.00"

