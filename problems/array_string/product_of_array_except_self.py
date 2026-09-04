class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Given an integer array nums, return an array answer such that answer[i] is equal
        to the product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        You must write an algorithm that runs in O(n) time and without using the division operation.

        Time Complexity: O(n)
        Space Complexity: O(1) auxiliary space (output array does not count towards extra space)
        """

        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
