"""
Problem: Reverse Linked List

Given the head of a singly linked list, reverse the list and
return the new head.

Approach:
Use three pointers (prev, curr, next) to reverse the links
iteratively. At each step, reverse the current node’s pointer
to point to the previous node.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next   # store next node
        curr.next = prev        # reverse the link
        prev = curr             # move prev forward
        curr = next_node        # move curr forward

    return prev
