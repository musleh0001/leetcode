from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Return the maximum profit from multiple stock buy/sell transactions.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        total_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]

        return total_profit
