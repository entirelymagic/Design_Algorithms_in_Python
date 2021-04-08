class Queue:
    """A Queue class.
        add: add the item to the last level of the stack.
        remove: get the last item from the top of the stack.
        its_empty: test if the stack is empty.
        length: return the number of levels of the stack.
        first_item: return the element from the top of the stack.
    """

    def __init__(self):
        """The constructor of the class"""
        self.items = []

    def __str__(self) -> str:
        """return a string representation of the items from the stack."""
        return str(self.items)

    def add(self, item) -> None:
        """Add the item to the last level of the stack."""
        self.items.append(item)

    def remove(self) -> object or None:
        """Get the last item from the top of the stack.
        If the stack is empty, will print that the stack is empty.
        """
        if len(self.items) > 0:
            return self.items.pop(0)  # use the pop() method from a list
        else:
            print("Stack is empty! \n")

    def its_empty(self) -> bool:
        """test if the stack is empty.
        @:return: bool
        """
        return self.items == []

    def length(self) -> int:
        """Return the number of levels of the stack."""
        return len(self.items)

    def first_item(self) -> object or None:
        """:return: the top element from the stack if not empty, else return None."""
        if len(self.items) > 0:
            return self.items[0]
        else:
            return None




