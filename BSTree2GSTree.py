"""Implements Convert BST to Greater Sum Tree

   Implementation for:
   http://algorithms.tutorialhorizon.com/convert-bst-to-greater-sum-tree/

"""


class Node:  # pylint: disable=too-few-public-methods
    """Implements a container node for building a binary tree"""

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


def insert(root, data):
    """Implements insert data into tree (BST)

       Assumes that root is valid Node containing data
         and that all all items in the tree are the same type
         (Integer assumed for Greater Sum Tree)
    """

    if root.data < data:
        if root.right is None:
            root.right = Node(data)
        else:
            insert(root.right, data)
    else:
        if root.left is None:
            root.left = Node(data)
        else:
            insert(root.left, data)


class BstToGst:
    """Class for Convert BST to Greater Sum Tree

       Note: A class wouldn't really be needed here except for the requirement
             to initialize the sum for each new instance.  Moving the sum to
             a module global seemed inappropriate because that exposes the inner
             workings of greater_tree()
    """

    def __init__(self):
        self.sum = 0

    def inorder(self, root):
        """Print an inorder traversal of the tree"""

        if root is not None:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def greater_tree(self, root):
        """Transforms Binary Search Tree at root to a Greater Sum Tree"""

        if root is not None:
            self.greater_tree(root.right)  # Traverse the right nodes first
            root.data, self.sum = self.sum, self.sum + root.data
            self.greater_tree(root.left)


def main():
    """Test Harness for Convert BST to Greater Sum Tree"""

    root = Node(10)
    insert(root, 5)
    insert(root, 15)
    insert(root, 2)
    insert(root, 7)
    insert(root, 12)
    insert(root, 20)
    gst = BstToGst()
    gst.inorder(root)
    gst.greater_tree(root)
    print()
    gst.inorder(root)
    print()


main()
