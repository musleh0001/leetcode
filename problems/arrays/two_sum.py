class Solution:
    def twoSum(self, nums: list[int], target: int):
        seen: dict[int, int] = {}

        for index, num in enumerate(nums):
            complements = target - num
            if complements in seen:
                return [seen[complements], index]
            seen[complements] = index
