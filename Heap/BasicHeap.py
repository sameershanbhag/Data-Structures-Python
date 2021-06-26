from typing import List

# Class definition for min heap (Object will be in ascending order)
class Heap:
    def __init__(self, current_heap: List):
        if current_heap:
            self.heap = current_heap
            self.heapifyDown()
        else:
            self.heap = []

    # Filler Methods
    @staticmethod
    def getLeftIndex(parent_index: int):
        """
        Return the Index of the left child in the binary tree
        :param parent_index: Int
        :return: int ( Index of left child )
        """
        return 2 * parent_index + 1

    @staticmethod
    def getRightIndex(parent_index: int):
        """
        Return the Index of the right child in the binary tree
        :param parent_index: Int
        :return: int ( Index of right child )
        """
        return 2 * parent_index + 2

    @staticmethod
    def getParentIndex(child_index: int):
        """
        Return the index of parent
        :param child_index: int index of left/right child
        :return: int ( Index of parent )
        """
        return child_index - 1 // 2

    def hasLeftChild(self, index: int):
        """
        Check if the element has left child
        :param index: int
        :return: bool
        """
        return self.getLeftIndex(index) < len(self.heap)

    def hasRightChild(self, index: int):
        """
        Check if the current element has a Right child
        :param index: int
        :return: bool
        """
        return self.getRightIndex(index) < len(self.heap)

    def hasParent(self, index: int):
        """
        check if the current element has a parent
        :param index: int
        :return: bool
        """
        return self.getParentIndex(index) >=  0

    def leftChild(self, index: int):
        """
        Get the value of the left child (if exist)
        :param index: int
        :return: int
        """
        return self.heap[self.getLeftIndex(index)]

    def rightChild(self, index: int):
        """
        Get the value of the right child (if exist)
        :param index: int
        :return: int
        """
        return self.heap[self.getRightIndex(index)]

    def parent(self, index: int):
        """
        Get the value of the parent (if exist)
        :param index: int
        :return: int
        """
        return self.heap[self.getParentIndex(index)]

    """
    Functions that Actually does some work
    """
    def swap(self, current, swap):
        current_item = self.heap[current]
        self.heap[current] = self.heap[swap]
        self.heap[swap] = current_item

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            print('Heap is empty')

    def poll(self):
        if self.heap:
            current_item = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap = self.heap[:-1]
            self.heapifyDown()
            return current_item
        else:
            print('Heap is empty')

    def heap_pop(self):
        if self.heap:
            current_item = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap = self.heap[:-1]
            self.heapifyDown()
            return current_item
        else:
            print('Heap is empty')

    def heap_push(self, current: object):
        self.heap.append(current)
        self.heapifyUp()

    def heapifyDown(self) -> None:
        current_index = 0
        while self.hasLeftChild(current_index):
            smaller_index = self.getLeftIndex(current_index)
            if self.hasRightChild(current_index) and self.rightChild(current_index) > self.leftChild(current_index):
                smaller_index = self.getRightIndex(current_index)

            if self.heap[current_index] < self.heap[smaller_index]:
                break
            else:
                self.swap(current_index, smaller_index)

            current_index = smaller_index

    def heapifyUp(self) -> None:
        current_index = len(self.heap) - 1
        while self.hasParent(current_index) and self.parent(current_index) > self.heap[current_index]:
            self.swap(current_index, self.getParentIndex(current_index))
            current_index = self.getParentIndex(current_index)

    def nlargest(self, n: int):
        return self.heap[-n:]

    def nsmallest(self, n: int):
        return self.heap[:n+1]


if __name__ == '__main__':
    current = [10,9,8,7,6,5,4,3]
    current.reverse()
    solution = Heap(current)
    print(solution.heap)
    solution.heap_push(1)
    print(solution.heap)





