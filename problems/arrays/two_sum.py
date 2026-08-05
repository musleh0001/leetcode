class Solution:
    """
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for index, num in enumerate(nums):
            complements = target - num

            if complements in seen:
                return [seen[complements], index]
            seen[num] = index

        return []
