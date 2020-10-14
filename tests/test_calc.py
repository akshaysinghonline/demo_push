"""
Unit Tests for calc library
"""

import calc


class TestCalc:

    def test_add(self):
        assert 4 == calc.add(2, 2), "Should be 4"

    def test_sub(self):
        assert 2 == calc.sub(4, 2), "Should be 2"
