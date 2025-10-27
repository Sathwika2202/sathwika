class Stack:
    """A simple Stack implementation using a Python list.

    Supports typical stack operations: push, pop, peek, and is_empty.

    Attributes:
        items (list): The internal storage for stack elements.
    """

    def __init__(self):
        """Initializes an empty stack."""
        self.items = []

    def push(self, item):
        """Pushes an item onto the top of the stack.

        Args:
            item: The element to be added to the stack.
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the top item from the stack.

        Returns:
            The item on top of the stack.

        Raises:
            IndexError: If the stack is empty when attempting to pop.
        """
        if self.is_empty():
            # Better to raise an error if popping from an empty stack
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Returns the top item of the stack without removing it.

        Returns:
            The item on top of the stack.

        Raises:
            IndexError: If the stack is empty when attempting to peek.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Checks whether the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0


if __name__ == "__main__":
    # Test stack operations with sample data
    stack = Stack()
    print("Stack is empty? ", stack.is_empty())  # True
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top item (peek):", stack.peek())      # 30
    print("Pop item:", stack.pop())              # 30
    print("Pop item:", stack.pop())              # 20
    print("Stack is empty? ", stack.is_empty())  # False
    print("Pop item:", stack.pop())              # 10
    # This should raise an error:
    try:
        stack.pop()
    except IndexError as e:
        print("Error:", e)


"""
AI Suggestions:
---------------
- Optimization: For faster append/pop operations from both ends (especially for large stacks),
  consider using `collections.deque` instead of a list as its implementation is optimized for such operations.

- Alternative implementation example:

    from collections import deque

    class StackDeque:
        \"\"\"Stack implemented using collections.deque for optimized performance.\"\"\"
        def __init__(self):
            self.items = deque()
        def push(self, item):
            self.items.append(item)
        def pop(self):
            if not self.items:
                raise IndexError("pop from empty stack")
            return self.items.pop()
        def peek(self):
            if not self.items:
                raise IndexError("peek from empty stack")
            return self.items[-1]
        def is_empty(self):
            return not self.items

- For most simple use cases, a list-based stack is sufficient.
"""
