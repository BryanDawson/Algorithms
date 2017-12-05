"""Implements Single Threaded Binary Tree

   Implementation for:
   http://algorithms.tutorialhorizon.com/single-threaded-binary-tree-complete-implementation/

"""

class Node:  # pylint: disable=too-few-public-methods
    """Implements a container node for building a binary tree
       Note: a container class is usually deemed 'not pythonic' but
             is naturally expected for tree implementations
    """

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data
        self.rightthread = False


def insert(root, data):
    """Inserts the node and sets the thread as needed"""

    newnode = Node(data)
    current = root
    while True:
        parent = current
        if data < current.data:
            current = current.left
            if not current:
                parent.left = newnode
                newnode.right = parent
                newnode.rightthread = True
                return
        elif not current.rightthread:
            current = current.right
            if current is None:
                parent.right = newnode
                return
        else:
            temp = current.right
            current.right = newnode
            current.rightthread = False
            newnode.right = temp
            newnode.rightthread = True
            return


def left_most_node(node):
    """Returns the left most node from the given node"""

    if node is None:
        return None
    else:
        while node.left is not None:
            node = node.left

    return node


def print_tree(root):
    """Inorder print of nodes in the tree"""

    current = left_most_node(root)

    # Traverse using the right pointers
    while current:
        print(current.data, end=' ')
        if current.rightthread:   # Node has no right child, move up to parent
            current = current.right
        else:  # Node has a right child, so traverse to that node's leftmost child
            current = left_most_node(current.right)

    print()


def main():
    """Test Harness for single thereaded binary tree"""

    root = Node(100)
    insert(root, 50)
    insert(root, 25)
    insert(root, 7)
    insert(root, 20)
    insert(root, 75)
    insert(root, 99)
    print(root.data)
    print(root.left.data)
    print_tree(root)

    root = Node()
    print_tree(root)

    root = Node(50)
    insert(root, 55)
    insert(root, 70)
    insert(root, 60)
    insert(root, 65)
    insert(root, 75)
    print_tree(root)


main()
