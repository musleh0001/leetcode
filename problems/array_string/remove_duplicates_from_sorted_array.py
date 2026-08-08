from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Modify nums in-place such that each unique element appears only once.
        Return the number of unique elements k.
        Two Pointers (Slow & Fast)

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        if not nums:
            return 0

        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k + 1
