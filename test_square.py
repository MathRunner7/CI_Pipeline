"""
This module will conduct test for a function square(number) from square.py
"""
from square import square
def test_square():
    testcase = 5
    op = square(testcase)
    assert op == 25
