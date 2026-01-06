"""
Problem: Merge Two Sorted Lists

Given two sorted singly linked lists, merge them into one
sorted list by reusing existing nodes.

Approach:
Use a dummy node and a tail pointer.
Compare nodes from both lists and attach the smaller one.
Once one list is exhausted, attach the remaining nodes.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

def merge_two_sorted_lists(list1, list2):
    dummy = ListNode(0)
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next
