class Node:
    """Representation of a node from binary tree"""
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.info = value


class BinarySearchTree:
    """Implementation of a binary tree structure."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
        else:
            currentNode = self.root

            if value < currentNode.info:
                # check if left none empty, if yes add it as left child node.
                if currentNode.left is None:
                    currentNode.left = newNode

                else:
                    # right
                    if currentNode.right is None:
                        currentNode.right = newNode

    def lookup(self, value):
        if not self.root:
            return False
        currentNode = self.root
        while currentNode:
            if value < currentNode.info:
                currentNode = currentNode.left
            elif value > currentNode.info:
                currentNode = currentNode.right
            elif value == currentNode.info:
                return currentNode.info
        return None



tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

print(tree.lookup(15))