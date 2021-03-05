# Design_Algorithms_in_Python

>I will be using TDD for the entire project.

## Chapter 1
1. Define a Rational class to create rational numbers from 2 integers
2. Raise `ZeroDivisionError` if denominator from Rational is not different from 0.
3. Create the method `__add__` in order to add`+` 2 rational numbers
    - Created a function `cmmnc` that given 2 numbers get the lowest denominator 
    - Apply the `cmmnc` function to the add function in order to get an irreducible fraction
    
4. Created `__eq__` to Rational class in order to check equality`==` of 2 Rational objects.
5. Check if numerator or denominator are integers, else raise error
6. Add `processed_numbers` to `Rational` that counts the total number of created rational numbers.
   - Changed from Exception to ValueError when denominator is 0.

7. Added `__sub__` method in order to perform subtraction`-` between Rational objects.
8. Added `__mul__` or method in order to perform multiplication`*` between Rational objects.
9. Added `__truediv__` method in order to perform division`/` between Rational objects.
10. Added `__floordiv__` method in order to perform floor division`//` between Rational objects.
10. Added `__iadd__` method in order to perform adding with`+=` between Rational objects.
10. Added `__isub__` method in order to perform `-=` between Rational objects.
10. Added `__imul__` method in order to perform `*=` between Rational objects.
10. Added `__ifloordiv__` method in order to perform `//=` between Rational objects.
