import pytest

from problems.array_string.best_time_to_buy_and_sell_stock_ii import Solution


@pytest.mark.parametrize(
    "prices, expected",
    [
        # Standard Example 1
        ([7, 1, 5, 3, 6, 4], 7),
        # Standard Example 2
        ([1, 2, 3, 4, 5], 4),
        # Standard Example 3
        ([7, 6, 4, 3, 1], 0),
        # Empty array
        ([], 0),
        # Single element
        ([5], 0),
        # Two elements - profit
        ([1, 5], 4),
        # Two elements - loss
        ([5, 1], 0),
        # All prices identical
        ([3, 3, 3, 3], 0),
        # Zigzag pattern
        ([1, 3, 2, 4, 3, 5], 6),
        # Multiple dips and peaks
        ([2, 1, 4, 5, 2, 9, 7], 11),
        # Flat then rise
        ([1, 1, 5, 5, 10], 9),
        # Large values
        ([10, 100, 10, 1000], 1080),
    ],
)
def test_max_profit_ii(prices, expected):
    sol = Solution()
    assert sol.maxProfit(prices) == expected
