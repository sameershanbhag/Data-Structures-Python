class LinkedList:
    """
    Introducing the Linked List class to store the data in a structured format
    """
    def __init__(self, value, next_ll=None):
        self.value = value
        self.next = next_ll


class Stack:
    """
    Implementing the Stack Data Structure utilizing Linked List
    """
    def __init__(self):
        """
        Initialize the linked list and the previous pointer
        """
        self.stack = LinkedList('None')
        self._previous = None

    def peek(self) -> any:
        """
        Displays the Head of the stack
        :return: obj, any
        """
        return self.stack.value

    def push(self, current_value: any) -> None:
        """
        Push the current element at the head of the stack
        :param current_value: (int) value to be inserted
        :return: obj, any
        """
        self._previous = self.stack
        self.stack.next = LinkedList(current_value)
        self.stack = self.stack.next

    def pop(self):
        """
        Retruns the element of at the head of the stack (if any)
        :return: str, obj, any
        """
        if self.stack.value == 'None':
            return "Already at the head of stack | Nothing to pop"
        current_value = self.stack.value
        self.stack = self._previous
        self.stack.next = None
        return current_value


if __name__ == "__main__":
    stack = Stack()
    print(f'Pop from Stack: {stack.pop()}')
    print(f'Current Head of the Stack: {stack.peek()}')
    print(f'Push `1` to Stack {stack.push(1)}')
    print(f'Current Head of the Stack: {stack.peek()}')
    print(f'Push `2` to Stack {stack.push(2)}')
    print(f'Push `3` to Stack {stack.push(3)}')
    print(f'Pop from Stack: {stack.pop()}')
    print(f'Current Head of the Stack: {stack.peek()}')