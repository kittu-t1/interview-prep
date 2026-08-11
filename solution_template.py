"""
Problem: Two Sum
Pattern: Hash Map
Difficulty: Easy

Problem Summary:
Given an array of integers and a target value, return the indices of the
two numbers that add up to the target.

Approach:
Use a dictionary to store numbers already seen while iterating through the
array. For each number, check whether its complement (target - number)
already exists in the dictionary. If it does, we've found our pair.

Time Complexity: O(n)
Space Complexity: O(n)

Learning:
When I need fast lookup while iterating through an array, consider a hash
map — it trades a bit of extra space for turning an O(n) search into O(1).
"""


def two_sum(nums, target):
    seen = {}  # value -> index

    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index

    return []  # no valid pair found


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # Expected: [0, 1]
    print(two_sum([3, 2, 4], 6))       # Expected: [1, 2]
