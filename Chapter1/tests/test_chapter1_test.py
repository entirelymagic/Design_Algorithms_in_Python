import pytest
from Chapter1.def_rational_numbers import Rational


class TestRationalClass:
    r1 = Rational(1, 8)
    r2 = Rational(1, 4)
    r3 = Rational(2, 16)
    Rational.processed_numbers -= 3

    @pytest.fixture()
    def rational(self):
        pass

    def test_value_errors(self):
        """
        Test if:
            - ValueError if numerator is not int
            - ValueError if denominator is not int
            - ValueError if denominator is 0
            -
        """

        with pytest.raises(ValueError):
            Rational(3, 0)
        with pytest.raises(ValueError):
            Rational('sal', 1)
        with pytest.raises(ValueError):
            Rational(1, 'hy')
        with pytest.raises(ValueError):
            Rational(1, 3.0)
        with pytest.raises(ValueError):
            Rational(5.0, 5)

    def test_rational_numbers_addition(self, rational):
        """Test if 2 rational numbers are returning the correct print value"""
        r3 = self.r1 + self.r2
        assert r3.__str__() == '3/8'

    def test_rational_number_equality(self):
        """Test to see comparison between 2 Rational objects"""
        assert self.r1 == self.r3
        assert self.r1 != self.r2

    def test_rational_number_subtraction(self):
        """Test __sub__ method for Rational objects"""
        assert self.r1 - self.r2

    def test_rational_number_multiplication(self):
        """test __mul__  method for Rational objects"""
        assert self.r1 * self.r2

    def test_rational_number_division(self):
        """test __truediv__  method for Rational objects"""
        assert self.r1 / self.r2

    def test_rational_number_floor_division(self):
        """test __floordiv__  method for Rational objects"""
        assert self.r1 // self.r2
