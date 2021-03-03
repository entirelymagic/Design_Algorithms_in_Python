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

    processed_numbers = 0

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

    def __add__(self, other_num: 'Rational') -> 'Rational':
        """Addition for 2 rational numbers(objects)"""

        resulted_numerator = self.a * other_num.b + self.b * other_num.a
        resulted_denominator = self.b * other_num.b
        # get the lowest common denominator
        lcd = cmmdc(resulted_numerator, resulted_denominator)
        # return the rational number as a irreducible fraction
        return Rational(int(resulted_numerator / lcd), int(resulted_denominator / lcd))

    def __eq__(self, other):
        """ Overload default __eq__ method.
        Test to see if 2 objects Rational are equal"""

        numerator1 = self.a * other.b
        numerator2 = other.a * self.b
        return numerator1 == numerator2

    def __sub__(self, other):
        """Overload default __sub__ method
        Perform subtraction between 2 Rational objects
        """
        resulted_numerator = self.a * other.b - self.b * other.a
        resulted_denominator = self.b * other.b
        # get lowest common denominator
        lcd = cmmdc(resulted_numerator, resulted_denominator)
        return Rational(resulted_numerator//lcd, resulted_denominator//lcd)
