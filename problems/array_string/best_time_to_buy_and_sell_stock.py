from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int | float:
        """
        Return the maximum profit from buying and selling stock on a single transaction.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
