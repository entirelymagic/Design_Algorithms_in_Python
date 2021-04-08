# Design_Algorithms_in_Python

> During this project I will create the project written in English as the book is in Romanian.  
> I will develop all the code using type hints and test driven development. 

## Chapter 1 - Object-Oriented Programming

> After finishing this chapter the reader will be able to:
> - define a class with attributes and instantiate an object.
> - overload operators and magic methods.
> - implement correctly the `__init__` and `__new__` constructors.
> - know how to use inheritance, polymorphism and overriding.


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


> After finishing this chapter the reader will be able to:
> - analyze the complexity of algorithms
> - chose between an algorithm with bigger complexity and one with lower complexity.
> - to identify the classes of complexity for algorithms
> - use asymptotic notations to characterize algorithms

2.1. Create 2 algorithms to read elements of a matrix and print tand return the results of total time it took and  
the total sum of the elements.

2.2. Create a `out.txt` files that will contain the matrix

2.3. Compare the results and add them to a csv files

2.4. Learning about algorithmic function analysis. 


## Chapter 3 - Lists, stacks, queues

> After finishing this chapter the reader will be able to:
> - identify the characteristics of data structures: lists, stacks, queues
> - implement algorithms that will be able to use the listed data structures
> - operate with generic lists, stacks and queues.

3.1. Created a OOP implementation of a stack class based on lists.

3.2. Created a OOP implementation of a queue class based on lists.

3.3 Solved Iosif Flavius problem using a queue