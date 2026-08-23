from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array,
        and return false if every element is distinct.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
