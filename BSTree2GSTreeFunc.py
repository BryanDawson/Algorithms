"""Implements Convert BST to Greater Sum Tree

   Implementation for:
   http://algorithms.tutorialhorizon.com/convert-bst-to-greater-sum-tree/

   Note: This version is an exercise in re-writing my first implementation to
         *not* use a class for BstToGst.  This means that the caller doesn't
         need to instantiate a class.  Not sure which implementation I prefer.

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


def inorder(root):
    """Print an inorder traversal of the tree"""

    if root is not None:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)


# NOTE: using a global _sum and an initializer function as an exercise in re-writing
#       the implementation to NOT use a class.
_sum = 0


def greater_tree(root):
    """Initialize the sum prior to recursive calls"""

    global _sum
    _sum = 0
    _greater_tree(root)


def _greater_tree(root):
    """Transforms Binary Search Tree at root to a Greater Sum Tree"""

    global _sum
    if root is not None:
        _greater_tree(root.right)  # Traverse the right nodes first
        root.data, _sum = _sum, _sum + root.data
        _greater_tree(root.left)


def main():
    """Test Harness for Convert BST to Greater Sum Tree"""

    root = Node(10)
    insert(root, 5)
    insert(root, 15)
    insert(root, 2)
    insert(root, 7)
    insert(root, 12)
    insert(root, 20)
    inorder(root)
    greater_tree(root)
    print()
    inorder(root)
    print()

    root = Node(10)
    insert(root, 5)
    insert(root, 15)
    insert(root, 2)
    insert(root, 7)
    insert(root, 12)
    insert(root, 20)
    inorder(root)
    greater_tree(root)
    print()
    inorder(root)
    print()


main()
