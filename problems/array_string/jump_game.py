from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Determine if you are able to reach the last index starting from index 0.

        :param nums: List[int] - Array of non-negative integers where each element represents your maximum jump length at that position.
        :return: bool - True if you can reach the last index, False otherwise.
        """

        max_reachable = 0

        for i, jump in enumerate(nums):
            if i > max_reachable:
                return False

            max_reachable = max(max_reachable, i + jump)

            if max_reachable >= len(nums) - 1:
                return True

        return True
