"""Series of exercises on reversing all or part of linked list

   Implements:
      Reverse a Linked List
      Reverse a Linked List — Part 2
      Reverse a Linked List in groups of given size ‘K’
      Reverse Alternative ‘k’ nodes in a Linked List.

   Implementation for:
   http://algorithms.tutorialhorizon.com/reverse-a-linked-list/
   http://algorithms.tutorialhorizon.com/reverse-a-linked-list-part-2/
   http://algorithms.tutorialhorizon.com/reverse-a-linked-list-in-groups-of-given-size-k/
   http://algorithms.tutorialhorizon.com/reverse-alternative-k-nodes-in-a-linked-list/

"""

# TODO: Finish implementations


# NOTE: class Node and class LinkedList implementations borrowed intact
#       (but with PEP8 fixes and other minor changes) from:
#        https://stackoverflow.com/a/3538133
class Node:   # pylint: disable=too-few-public-methods
    """Implements a container node for building linked lists"""

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return 'Node [' + str(self.value) + ']'


class LinkedList:
    """Implements a singly linked list"""

    def __init__(self, list_len=None):
        self.first = None
        self.last = None
        if list_len is not None:  # Build a default initial list
            for item in range(1, list_len+1):
                self.insert(item)

    def insert(self, data):
        """Implements insert data node into list"""

        if self.first is None:
            self.first = Node(data, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(data, None)
            self.first.next = self.last
        else:
            current = Node(data, None)
            self.last.next = current
            self.last = current

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [ ' + str(current.value) + ' '
            while current.next is not None:
                current = current.next
                out += str(current.value) + ' '
            return out + ']'
        return 'LinkedList []'

    def reverse(self):
        """Reverses the order of the linked list iteratively"""

        # Intialize current to head, prev to None
        curr_node, prev_node = self.first, None
        # Swap first and last now
        self.first, self.last = self.last, self.first

        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

    def reverse_recur(self):
        """Wraps the inner recursive version
           so that the two reverse methods have the same signature"""

        def _reverse_recur(current):
            """Reverses the order of the linked list recursively"""

            if current is None:
                return
            if current.next is None:
                self.first = current
                return
            _reverse_recur(current.next)
            current.next.next = current
            current.next = None
            self.last = current

        _reverse_recur(self.first)

    def reverse_groups(self, ksize=3):
        """Reverse Linked List in groups of given size ‘K’

           Note: default group size simplifies test harness
        """
        # TODO: finish implementation
        print(ksize)
        return

    def clear(self):
        """Implements clear out linked list"""
        self.__init__()


def main():
    """Test Harness for linked list manipulations"""

    # Tuple of functions drives the test cases.
    #  Comment out any that should not be run.
    testcases = (
        LinkedList.reverse,
        LinkedList.reverse_recur,
        LinkedList.reverse_groups
    )

    for func in testcases:
        print("\nTesting: ", func.__name__)
        link_list = LinkedList(8)
        print("Initial List:", link_list)
        print("first:", link_list.first.value, "last:", link_list.last.value)
        func(link_list)
        print("Reversed List: ", link_list)
        print("first:", link_list.first.value, "last:", link_list.last.value)
        print("Confirm success on empty list case...")
        link_list.clear()
        func(link_list)
        print(link_list)


main()
