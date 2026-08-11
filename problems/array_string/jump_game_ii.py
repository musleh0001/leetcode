from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Return the minimum number of jumps to reach the last index.

        :param nums: List[int] - Array of non-negative integers where nums[i] is max jump length from index i.
        :return: int - Minimum number of jumps required to reach nums[n - 1].
        """

        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_jump_end = 0
        max_reachable = 0

        for i in range(n - 1):
            max_reachable = max(max_reachable, i + nums[i])

            if i == current_jump_end:
                jumps += 1
                current_jump_end = max_reachable

                if current_jump_end >= n - 1:
                    break

        return jumps
