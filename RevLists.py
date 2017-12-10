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

    def __init__(self):
        self.first = None
        self.last = None

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

    def clear(self):
        """Implements clear out linked list"""
        self.__init__()


def main():
    """Test Harness for linked list manipulations"""

    # Tuple controls which test cases run. Comment any that should not run.
    testcases = (
        'list',
        'rev',
        'rev2',
        'revk',
        'revak'
    )

    if 'list' in testcases:
        link_list = LinkedList()
        link_list.insert(1)
        link_list.insert(1)
        link_list.insert(2)
        link_list.insert(4)
        print(link_list)
        link_list.clear()
        print(link_list)


main()
