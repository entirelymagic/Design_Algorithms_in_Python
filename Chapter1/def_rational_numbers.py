"""
A rational number (Q) is the division of 2 integer numbers a nad b:
rational = a / b where b is not null(None in python).
The rational Number has a finite umber of digits or eventually begins to repeat
the same finite sequence of digits over and over again.

Real numbers (R) that are not rational are irrational numbers ( pi, e , golden ratio).
"""
from typing import Type
from Chapter1.functions import cmmdc


class Rational:
    """
    A rational class that takes a numerator 'a' and a denominator 'b'
    @:param a:int - Required numerator
    @:param b:int - Required denominator

    @:raise Error if b==0
    """

    processed_numbers: int = 0

    def __init__(self, a: int, b: int) -> None:
        if type(a) is not int:
            raise ValueError("Numerator is not an integer")
        elif type(b) is not int:
            raise ValueError("Denominator is not an integer")
        elif b == 0:
            raise ValueError("Denominator is equal to 0")
        else:
            self.a = a
            self.b = b
            # add a new processed number.
            Rational.processed_numbers += 1

    def __str__(self) -> str:
        """Overload default __str__ method.
        :return: The string representation of the rational number.
        """

        return str(self.a) + '/' + str(self.b)

    @staticmethod
    def _irreducible_fraction(a: int, b: int,) -> 'Rational':
        """Take numerator and denominator for Rational object
        and return it after checking if it a irreducible fraction.
        """
        lcd = cmmdc(a, b)
        return Rational(a // lcd, b // lcd)

    def __add__(self, other_num: 'Rational') -> 'Rational':
        """Addition for 2 rational numbers(objects)"""

        resulted_numerator = self.a * other_num.b + self.b * other_num.a
        resulted_denominator = self.b * other_num.b
        # return a Rational number after it is checked that it is not a irreducible_fraction
        return self._irreducible_fraction(resulted_numerator, resulted_denominator)

    def __eq__(self, other: 'Rational') -> bool:
        """ Overload default __eq__ method.
        Test to see if 2 objects Rational are equal"""

        numerator1 = self.a * other.b
        numerator2 = other.a * self.b
        return numerator1 == numerator2

    def __sub__(self, other: 'Rational') -> 'Rational':
        """Overload default __sub__ method
        Perform subtraction between 2 Rational objects
        """
        resulted_numerator = self.a * other.b - self.b * other.a
        resulted_denominator = self.b * other.b
        # return a Rational number after it is checked that it is not a irreducible_fraction
        return self._irreducible_fraction(resulted_numerator, resulted_denominator)

    def __mul__(self, other: 'Rational'):
        """Overload default __sub__ method
        Perform Multiplication between 2 Rational objects
        """
        resulted_numerator = self.a * other.a
        resulted_denominator = self.b * other.b
        # return a Rational number after it is checked that it is not a irreducible_fraction
        return self._irreducible_fraction(resulted_numerator, resulted_denominator)

