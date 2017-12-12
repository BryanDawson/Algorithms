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

# TODO: Complete the implementations

class Node:  # pylint: disable=too-few-public-methods
    """Implements a container node for building linked lists"""

    def __init__(self, data=None):
        self.next = None
        self.data = data


def insert(head, data):
    """Implements insert data into list

       Assumes that head points to a valid node
    """

    if head.next is None:
        head.next = Node(data)
    else:
        insert(head.next, data)


def list_print(head):
    """Simple printout of linked list"""

    print("Linked List [ ", end='')
    while head is not None:
        print(head.data, end=' ')
        head = head.next
    print(']')


def build_range(count):
    """Build a linked list initialized with range 1 to count"""

    head = Node(1)
    for item in range(2, count+1):
        insert(head, item)
    return head


def reverse(head):
    """Reverses the order of the linked list iteratively"""

    # Intialize current to head, prev to None
    curr_node, prev_node = head, None

    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node


def reverse_recur(current):
    """Reverses the order of the linked list recursively"""

    if current is None:
        return None
    if current.next is None:
        return current
    head = reverse_recur(current.next)
    current.next.next = current
    current.next = None
    return head


def reverse_groups(head, group_size):
    """Reverse a Linked List in groups of given size ‘K’"""

    # Intialize current to head, prev to None
    curr_node, prev_node, next_node = head, None, None
    count = group_size

    while curr_node is not None and count > 0:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
        count -= 1

    if next_node is not None:
        head.next = reverse_groups(next_node, group_size)

    return prev_node


def main():
    """Test Harness for exercises on reversing all or part of linked list"""

    print("Testing reverse:")
    link_list = build_range(8)
    list_print(link_list)
    link_list = reverse(link_list)
    list_print(link_list)
    print("\nTesting reverse_recur:")
    list_print(link_list)
    link_list = reverse_recur(link_list)
    list_print(link_list)
    print("\nTesting reverse_groups:")
    list_print(link_list)
    link_list = reverse_groups(link_list, 3)
    list_print(link_list)


main()
