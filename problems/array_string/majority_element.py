from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int | None:
        """
        Return the majority element that appears more than ⌊n / 2⌋ times.
        Boyer-Moore Voting Algorithm.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
