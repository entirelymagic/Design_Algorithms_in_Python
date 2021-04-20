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

3.3. Solved Iosif Flavius problem using a queue.

## Chapter 4 - Undirected Graphs

> After finishing this chapter the reader will be able to:
> - identify concept characteristics(node, edge, grade, chain, cycle, partial graph etc)
> - implement algorithms that shape information using structured data
> - we go through a graph in height and width
> - operate with generic types of graphs.

4.1. Undirected graph

Types of a Graph:
> - regulated graph: it's an undirected graph in which the nodes have equal grades.
> - acyclic graph: it's an undirected graph in which the nodes have.
> - complete graph: a graph that has any two distinct nodes who are adjacent. In a complete graph the grade of any node
> is  `n-1` and the number of edges is `m = n * (n-1)/2`.
> - null graph: an undirected graph that has the set of edges void. All edges are isolated.
> - bipartite graph: an undirected graph `G = (X, U)`
> - hamiltonian graph: an undirected graph that contain at least 1 hamiltonian cycle.:
>   - an undirected graph with `n` edges, and the grade of the tip is equal or greater then `n/2` is hamiltonian
>   - given an elemental chain `[i1, i2, ..., in]` which goes through all nodes of an undirected graph,
>   if `(d(i1) + d(in)) >= n`, then the graph is hamiltonian.
>   - for any adjacent pair of nodes `i!=j`, we have `(d(i) + d(j)) >= n`, then the graph is hamiltonian.
> - eulerian graph: an undirected graph that contain a eulerian circle.
>   - a chain of an undirected graph that contain each edge once and only once is called eulerian chain.
>   - a graph is eulerian if and only if all the peaks are isolated, it is connected 

## Chapter 5 - oriented graphs

An oriented graph is an ordered pair `G= (X, U)` where X is the finite set and not null. 
U is a set of ordered pairs of distinct elements of X named arcs.


> After finishing this chapter the reader will be able to:
> - identify the characteristic concepts of data structures of type: oriented graphs.
> - implement algorithms that model the information using oriented graph data structures.


5.1. Circuit:
> - A circuit is an ordered graph in which the path from the initial node coincide with the end node 
> - An elementary circuit is a circuit in which, exception the extremities, the nodes do not repeat.

5.2. Chain:
> - in an oriented graph, it is called a chain if a succession of arches `(i1, i2), (i2, i3), ..., (ik-1, ik)` noted
> (i1, i2, ik) with the properties that any 2  consecutive arches have a common extremity( does not matter the orientation).

5.3. A connected graph 
> - is a graph that is connected in the sense of a topological space, i.e., there is a path from any
> point to any other point in the graph. A graph that is not connected is said to be disconnected. This definition means that the null graph and singleton graph are considered connected, while empty graphs on n>=2 nodes are disconnected.


## Chapter 6 - Tree-structures

> After finishing this chapter the reader will be able to:
> - identify concepts characteristic to tree structures
> - implement algorithms that model the information using data tree structures
> - traverse tree structure data

