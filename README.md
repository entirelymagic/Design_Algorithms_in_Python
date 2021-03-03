# Design_Algorithms_in_Python

## Chapter 1
1. Define a Rational class to create rational numbers from 2 integers
2. Raise `ZeroDivisionError` if denominator from Rational is not different from 0.
3. Create the method __add__ in order to add 2 rational numbers
    - Created a function `cmmnc` that given 2 numbers get the lowest denominator 
    - Apply the `cmmnc` function to the add function in order to get an irreducible fraction
    
4. Created `__eq__` to Rational class in order to check if 2 Rational objects are equal or not.
5. Check if numerator or denominator are integers, else raise error
6. Add `processed_numbers` to `Rational` that counts the total number of created rational numbers.
   - Changed from Exception to ValueError when denominator is 0.

7. Added `__sub__` method in order to perform subtraction for Rational objects.

