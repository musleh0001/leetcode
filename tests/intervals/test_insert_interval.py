import pytest

from problems.intervals.insert_interval import Solution


@pytest.mark.parametrize(
    "intervals, new_interval, expected",
    [
        # Standard Example 1
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        # Standard Example 2
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
        # Empty intervals list
        ([], [5, 7], [[5, 7]]),
        # Insert before all intervals (no overlap)
        ([[3, 5], [6, 9]], [1, 2], [[1, 2], [3, 5], [6, 9]]),
        # Insert after all intervals (no overlap)
        ([[1, 2], [3, 5]], [6, 8], [[1, 2], [3, 5], [6, 8]]),
        # Insert in between two intervals (no overlap)
        ([[1, 2], [7, 9]], [4, 5], [[1, 2], [4, 5], [7, 9]]),
        # New interval covers all existing intervals
        ([[2, 3], [5, 7], [8, 9]], [1, 10], [[1, 10]]),
        # Single interval in list with overlap
        ([[1, 5]], [2, 3], [[1, 5]]),
        # New interval touches boundary at start
        ([[1, 3], [6, 9]], [3, 5], [[1, 5], [6, 9]]),
        # New interval touches boundary at end
        ([[1, 3], [6, 9]], [5, 6], [[1, 3], [5, 9]]),
        # Point interval inserted (start == end)
        ([[1, 5]], [2, 2], [[1, 5]]),
        # Point interval inserted into disjoint point intervals
        ([[1, 1], [3, 3]], [2, 2], [[1, 1], [2, 2], [3, 3]]),
        # Duplicate identical interval
        ([[1, 5]], [1, 5], [[1, 5]]),
        # Extreme / large boundaries
        ([[0, 10], [20, 30]], [10, 20], [[0, 30]]),
    ],
)
def test_insert_interval(intervals, new_interval, expected):
    sol = Solution()
    assert sol.insert(intervals, new_interval) == expected
