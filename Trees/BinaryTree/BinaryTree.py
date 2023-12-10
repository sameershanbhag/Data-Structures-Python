class Node:
    def __init__(self, value=None, left=None, right=None):
        """
        Initialize a Node in a binary tree.

        Parameters:
        value (optional): The value stored in the node.
        left (Node, optional): Reference to the left child Node.
        right (Node, optional): Reference to the right child Node.
        """
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        """
        Initialize a BinaryTree with root set to None.
        """
        self.root = None

    def add(self, value):
        """
        Add a value to the binary tree. If the tree is empty,
        the value becomes the root. Otherwise, add it using
        the _add helper method.

        Parameters:
        value: The value to be added to the tree.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        """
        Recursive helper method to add a value to the tree
        at the correct location.

        Parameters:
        value: The value to be added.
        node: The current node being examined.
        """
        if value < node.value:
            if node.left:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        elif value > node.value:
            if node.right:
                self._add(value, node.right)
            else:
                node.right = Node(value)

    def find(self, value):
        """
        Find a value in the binary tree. Returns a message
        indicating whether the value was found.

        Parameters:
        value: The value to be searched in the tree.
        """
        if self.root is None:
            return "Not Found"

        return self._find(value, self.root)

    def _find(self, value, node):
        """
        Recursive helper method to find a value in the tree.

        Parameters:
        value: The value being searched for.
        node: The current node being examined.
        """
        if node.value == value:
            return f"Found {value}"
        else:
            if value < node.value:
                if node.left:
                    return self._find(value, node.left)
                else:
                    return "Not Found"
            elif value > node.value:
                if node.right:
                    return self._find(value, node.right)
                else:
                    return "Not Found"


if __name__ == '__main__':
    binary_tree_elements = [1, 4, 5, 6, 7, 2, 4, 56, 67, 234, 234, 22, 14, 5]
    final_node = BinaryTree()

    for val in binary_tree_elements:
        final_node.add(val)

    print(final_node.find(15))
