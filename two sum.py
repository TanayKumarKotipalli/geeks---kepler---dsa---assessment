"""
Problem: Two Sum

Approach:
Use a hashmap to store numbers seen so far.
For each number, check if the complement exists.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
