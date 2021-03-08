### Functions to access instance attributes.
#### `f1 = R(1,2) `- Rational object.

- Get an attributes by its name:  
`getattr(f1, 'a')` - will return `1`.
- Check if an attribute exists:  
`hasattr(f1, 'a')`
- Modify a value of an attribute:  
`setattr(f1, 'a',)`
- Delete an attribute of an object:  
`delattr(f1, 'a',)`

> Delete an attribute or an object or a class using `del`   
> - `del f1.a`  - delete the attribute `a` from the object `f1`  
> - `del f1` - delete the object `f1`
> - `del Rational` - delete the `Rational` class

### The `__new__` Constructor

- The `__new__` constructor is called when the object is created.
- The `__init__` method is called when the object is instantiated.
- The `__new__` and `__init__` are considered together to be the constructor of the object.

