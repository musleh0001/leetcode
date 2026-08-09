from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Modify nums in-place such that each unique element appears at most twice.
        Return the number of elements k after modification.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        if len(nums) <= 2:
            return len(nums)

        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k
