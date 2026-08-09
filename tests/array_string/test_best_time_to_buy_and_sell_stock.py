import pytest

from problems.array_string.best_time_to_buy_and_sell_stock import Solution


@pytest.mark.parametrize(
    "prices, expected",
    [
        # Standard Example 1
        ([7, 1, 5, 3, 6, 4], 5),
        # Standard Example 2
        ([7, 6, 4, 3, 1], 0),
        # Empty array
        ([], 0),
        # Single element
        ([5], 0),
        # Two elements - profit
        ([1, 5], 4),
        # Two elements - loss
        ([5, 1], 0),
        # Monotonically increasing
        ([1, 2, 3, 4, 5], 4),
        # All prices identical
        ([3, 3, 3, 3], 0),
        # Minimum price at end
        ([3, 10, 1, 2], 7),
        # Multiple peaks
        ([2, 4, 1, 7, 3], 6),
        # Large values
        ([10000, 1, 20000], 19999),
        # Flat then rise
        ([5, 5, 5, 10], 5),
    ],
)
def test_max_profit(prices, expected):
    sol = Solution()
    assert sol.maxProfit(prices) == expected
