import pytest
from Chapter1.def_rational_numbers import Rational


class TestRationalClass:

    @pytest.fixture
    def r1(self):
        r1 = Rational(1, 8)
        return r1

    @pytest.fixture
    def r2(self):
        r2 = Rational(1, 4)
        return r2

    @pytest.fixture
    def r3(self):
        r3 = Rational(1, 8)
        return r3

    # def test_value_errors(self):
    #     """
    #     Test if ValueError when __new__ constructor is not implemented:
    #         - ValueError if numerator is not int
    #         - ValueError if denominator is not int
    #         - ValueError if denominator is 0
    #         -
    #     """
    #
    #     with pytest.raises(ValueError):
    #         Rational(3, 0)
    #     with pytest.raises(ValueError):
    #         Rational('sal', 1)
    #     with pytest.raises(ValueError):
    #         Rational(1, 'hy')
    #     with pytest.raises(ValueError):
    #         Rational(1, 3.0)
    #     with pytest.raises(ValueError):
    #         Rational(5.0, 5)

    def test_rational_numbers_are_set_to_None_if_values_are_not_valid(self):
        """Test if the return is none for the denominator or numerator incorrect values"""
        f1 = Rational(4, 0)
        f2 = Rational(2.1, 5)
        f3 = Rational(3, 6.2)
        f4 = Rational('a', 2)
        f5 = Rational(3, 'b')
        assert f1 is None
        assert f2 is None
        assert f3 is None
        assert f4 is None
        assert f5 is None

    def test_rational_numbers_addition(self, r1, r2):
        """Test if 2 rational numbers are returning the correct print value"""
        r3 = r1 + r2
        assert r3.__str__() == '3/8'

    def test_rational_number_equality(self, r1, r2, r3):
        """Test to see comparison between 2 Rational objects"""
        assert r1 == r3
        assert r1 != r2

    def test_rational_number_subtraction(self, r1, r2):
        """Test __sub__ method for Rational objects"""
        result = r1 - r2
        assert result.__str__() == '-1/8'

    def test_rational_number_multiplication(self, r1, r2):
        """test __mul__  method for Rational objects"""
        result = r1 * r2
        assert result.__str__() == '1/32'

    def test_rational_number_division(self, r1, r2):
        """test __truediv__  method for Rational objects"""
        result = r1 / r2
        assert result == 0.5

    def test_rational_number_floor_division(self, r1, r2):
        """test __floordiv__  method for Rational objects"""
        assert r1 // r2

    def test_rational_number_iadd(self, r1, r2):
        """test __iadd__  method for Rational objects"""
        r1 = Rational(1, 8)
        r1 += r2
        assert r1.__str__() == "3/8"

    def test_rational_number_isub(self, r1, r2):
        """test __isub__  method for Rational objects"""
        r1 = Rational(1, 8)
        r1 -= r2
        assert r1.__str__() == "-1/8"

    def test_rational_number_imul(self, r1, r2):
        """test __imul__  method for Rational objects"""
        r1 = Rational(1, 8)
        r1 *= r2
        assert r1.__str__() == "1/32"

    def test_rational_number_ifloordiv(self, r1, r2):
        """test __ifloordiv__  method for Rational objects"""
        r1 //= r2
        assert r1.__str__() == "1/2"

    def test_rational_number_gt(self, r1, r2):
        """Test if 2 rational objects can use __gt__ method"""
        assert r2 > r1

    def test_rational_number_ge(self, r1, r3):
        """Test if 2 rational objects can use __ge__ method"""
        assert r3 >= r1

    def test_rational_number_lt(self, r1, r2):
        """Test if 2 rational objects can use __lt__ method"""
        assert r1 < r2

    def test_rational_number_le(self, r1, r2):
        """Test if 2 rational objects can use __le__ method"""
        assert r1 <= r2

    def test_rational_number_ne(self, r1, r2):
        """Test if 2 rational objects can use __ne__ method"""
        assert r2 != r1

    def test_get_numerator(self, r1):
        """Test to see if given a rational object it can return it's numerator"""
        assert r1.numerator == 1

    def test_get_denominator(self, r1):
        """Test to see if given a rational object it can return it's denominator"""
        assert r1.denominator == 8

    def test_get_decimal_form(self, r1):
        """Test to see if given a rational object it can return it's decimal form"""
        assert r1.decimal_form == 0.125
