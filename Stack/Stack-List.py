"""
This is the most basic implementation of the stack with List (ArrayList) data structure
"""


class Stack:
    def __init__(self) -> None:
        """
        Initialize the Stack
        """
        self.stack = list()

    def peek(self) -> any:
        """
        Return the latest element in the stack as its Last In First Out
        :return: obj, any
        """
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def push(self, current_element: any) -> None:
        """
        Insert the current element at the head of the stack
        :param current_element: obj, any
        :return: None
        """
        self.stack.append(current_element)

    def pop(self) -> any:
        """
        Return and remove the element from the top of the stack as LIFO
        :return: obj, any
        """
        return self.stack.pop()


if __name__ == "__main__":
    stack = Stack()
    print(f'Current Head of the Stack: {stack.peek()}')
    print(f'Push `1` to Stack {stack.push(1)}')
    print(f'Current Head of the Stack: {stack.peek()}')
    print(f'Push `2` to Stack {stack.push(2)}')
    print(f'Push `3` to Stack {stack.push(3)}')
    print(f'Pop from Stack: {stack.pop()}')
    print(f'Current Head of the Stack: {stack.peek()}')