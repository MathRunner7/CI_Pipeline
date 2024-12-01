"""
This module will conduct test for a function square(number) from square.py
"""
from cube import cube
def test_square():
    testcase = 5
    op = cube(testcase)
    assert op == 125
