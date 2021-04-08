class Stack:
    """A stack class.
        push: add the item to the last level of the stack.
        pop: get the last item from the top of the stack.
        its_empty: test if the stack is empty.
        height: return the number of levels of the stack.
        top_stack: return the element from the top of the stack.
        show_stack: show the content of the stack from the top to the bottom of the stack.
    """

    def __init__(self):
        """The constructor of the class"""
        self.items = []

    def show_stack(self) -> None:
        """Show the content of the stack from the top to the bottom of the stack."""
        print("Show stack: ")
        ok = 1
        for i in reversed(self.items):
            print(i)
            ok = 0
        if ok:
            print("The stack is empty!")
        print("\n")

    def push(self, item) -> None:
        """Add the item to the last level of the stack."""
        self.items.append(item)

    def pop(self) -> object or None:
        """Get the last item from the top of the stack.
        If the stack is empty, will print that the stack is empty.
        """
        if len(self.items) > 0:
            return self.items.pop()  # use the pop() method from a list
        else:
            print("Stack is empty! \n")

    def its_empty(self) -> bool:
        """test if the stack is empty.
        @:return: bool
        """
        return self.items == []

    def height(self) -> int:
        """Return the number of levels of the stack."""
        return len(self.items)

    def top_stack(self) -> object or None:
        """:return: the top element from the stack if not empty, else return None."""
        if len(self.items) > 0:
            return self.items[len(self.items)-1]
        else:
            return None




