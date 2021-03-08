# Design_Algorithms_in_Python

> During this project I will create the project written in English as the book is in Romanian.
> I will develop all the code using type hints and test driven development.  

## Chapter 1 - Object Oriented Programming
1.1. Define a Rational class to create rational numbers from 2 integers

1.2. Raise `ZeroDivisionError` if denominator from Rational is not different from 0.

1.3. Create the method `__add__` in order to add`+` 2 rational numbers
    - Created a function `cmmnc` that given 2 numbers get the lowest denominator 
    - Apply the `cmmnc` function to the add function in order to get an irreducible fraction
    
1.4. Created `__eq__` to Rational class in order to check equality`==` of 2 Rational objects.

1.5. Check if numerator or denominator are integers, else raise error

1.6. Add `processed_numbers` to `Rational` that counts the total number of created rational numbers.
   - Changed from Exception to ValueError when denominator is 0.

1.7. Added `__sub__` method in order to perform subtraction`-` between Rational objects.

1.8. Added `__mul__` or method in order to perform multiplication`*` between Rational objects.

1.9. Added `__truediv__` method in order to perform division`/` between Rational objects.

1.10. Added `__floordiv__` method in order to perform floor division`//` between Rational objects.

1.11. Added `__iadd__` method in order to perform adding with`+=` between Rational objects.

1.12. Added `__isub__` method in order to perform `-=` between Rational objects.

1.13. Added `__imul__` method in order to perform `*=` between Rational objects.

1.14. Added `__ifloordiv__` method in order to perform `//=` between Rational objects.

1.15. Added `__gt__`, `__ge__`, `__lt__`, `__le__`, `__ne__` opperations between Rational objects.

1.16. Added `numerator`, `denominator`, `decilaml_form` as properties of Rational objects.

1.17. Implement `__new__` constructor to return a null object if the parameters of the class are not int or 0 as 
denominator.

## Chapter 2 - Algorithm analysis

