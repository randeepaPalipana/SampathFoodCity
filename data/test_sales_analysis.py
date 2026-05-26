import pytest

def discount(price):
    
    if price >= 10000:
        return price * 5 / 100
    else:
        return 0

def test_discount():
    assert discount(15000) == 1500  
