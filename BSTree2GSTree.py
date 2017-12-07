"""Implements Convert BST to Greater Sum Tree

   Implementation for:
   http://algorithms.tutorialhorizon.com/convert-bst-to-greater-sum-tree/

"""

# TODO: Finish implentation of BST to GST

class Node:  # pylint: disable=too-few-public-methods
    """Implements a container node for building a binary tree"""

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


def insert(root, data):
    """Implements insert data into tree

       Assumes that root is valid Node containing data
         and that all all items in the tree are the same type
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
    if root is not None:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)


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
    print()

    root = Node("blue")
    insert(root, "red")
    insert(root, "green")
    insert(root, "yellow")
    inorder(root)



main()
