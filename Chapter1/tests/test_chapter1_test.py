import pytest
from Chapter1.def_rational_numbers import Rational


class TestRationalClass:
    r1 = Rational(1, 8)
    r2 = Rational(1, 4)
    r3 = Rational(2, 16)

    @pytest.fixture()
    def rational(self):
        rational1 = Rational(1, 2)
        return rational1

    def test_error_0_as_denominator(self):
        """Test if given 0 as denominator for Rational Object raises an Error."""
        with pytest.raises(Exception):
            Rational(3, 0)

    def test_rational_numbers_addition(self, rational):
        """Test if 2 rational numbers are returning the correct print value"""
        r3 = self.r1 + self.r2
        assert r3.__str__() == '3/8'

    def test_rational_number_equality(self):
        """Test to see comparison between 2 Rational objects"""
        assert self.r1 == self.r3
        assert self.r1 != self.r2


