"""Implements Single Threaded Binary Tree

   Implementation for:
   http://algorithms.tutorialhorizon.com/single-threaded-binary-tree-complete-implementation/

"""

# TODO: Implementation still in progress.


class Node:
    """Implements a container node for building a binary tree"""
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data
        self.rightthread = False


class SingleThreadedBinaryTree:
    """Implements basic single threaded binary tree"""

    def insert(self, root, data):
        newnode = Node(data)
        current = root
        while True:
            parent = current
            if data < current.data:
                current = current.left
                if current == None:
                    parent.left = newnode
                    newnode.right = parent
                    newnode.rightthread = True
                    return
            elif current.rightthread == False:
                current = current.right
                if current == None:
                    parent.right = newnode
                    return
            else:
                temp = current.right
                current.right = newnode
                newnode.right = temp
                newnode.rightthread = True
                return


def main():
    """Test Harness for single thereaded binary tree"""

    root = Node(100)
    st = SingleThreadedBinaryTree()
    st.insert(root, 50)
    print(root.data)
    print(root.left.data)
    pass


main()
