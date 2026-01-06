"""
Problem: Contains Duplicate

Given an integer array nums, return True if any value appears
at least twice in the array, and return False if every element is distinct.

Approach:
Use a set to keep track of elements seen so far.
If an element is already present in the set, a duplicate exists.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False
