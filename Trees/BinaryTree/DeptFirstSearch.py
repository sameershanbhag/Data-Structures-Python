from BinaryTree import BinaryTree


class DFS:
    def __init__(self, tree_vals: list):
        self.binaryTree = BinaryTree()

        # generating the binary tree
        for val in tree_vals:
            self.binaryTree.add(val)

        self.values_stack = []
        self.values_recurse = []

    def dfs_stack(self):
        """
        Depth First Search using a stack.
        :return:
        """
        stack = [self.binaryTree.root]
        while stack:
            current = stack.pop()
            self.values_stack.append(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return self.values_stack

    def dfs_recursion(self, node):
        """
        Depth First Search using recursion.
        :param node: The current node being examined.
        :return:
        """
        if node:
            self.values_recurse.append(node.value)
            self.dfs_recursion(node.left)
            self.dfs_recursion(node.right)
        return self.values_recurse


if __name__ == "__main__":
    tree = [1, 4, 5, 6, 7, 2, 4, 56, 67, 234, 234, 22, 14, 5]
    dfs = DFS(tree)
    print(dfs.dfs_stack())
    print(dfs.dfs_recursion(dfs.binaryTree.root))
