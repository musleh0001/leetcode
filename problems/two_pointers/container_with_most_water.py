class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        You are given an integer array height of length n. There are n vertical lines
        drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

        Find two lines that together with the x-axis form a container, such that the
        container contains the most water.

        Return the maximum amount of water a container can store.

        Area = (right - left) x min(height[left], height[right])

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            max_water = max(max_water, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
