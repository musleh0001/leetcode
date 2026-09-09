import pytest

from problems.intervals.merge_intervals import Solution


@pytest.mark.parametrize(
    "intervals, expected",
    [
        # Standard Example 1
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        # Standard Example 2 (touching boundaries)
        ([[1, 4], [4, 5]], [[1, 5]]),
        # Single interval
        ([[1, 4]], [[1, 4]]),
        # Already non-overlapping and sorted
        ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),
        # Completely overlapping (all merge into one)
        ([[1, 10], [2, 3], [4, 8], [9, 10]], [[1, 10]]),
        # Unsorted input intervals
        ([[8, 10], [1, 3], [15, 18], [2, 6]], [[1, 6], [8, 10], [15, 18]]),
        # Subsets / fully nested intervals
        ([[1, 4], [2, 3]], [[1, 4]]),
        # Point intervals (start == end) with overlap
        ([[1, 1], [1, 1], [1, 2]], [[1, 2]]),
        # Disjoint point intervals
        ([[1, 1], [2, 2], [3, 3]], [[1, 1], [2, 2], [3, 3]]),
        # All identical intervals
        ([[2, 5], [2, 5], [2, 5]], [[2, 5]]),
        # Chain of overlapping intervals in reverse order
        ([[4, 5], [3, 4], [2, 3], [1, 2]], [[1, 5]]),
        # Boundary / extreme coordinate values
        ([[0, 10000], [10000, 20000]], [[0, 20000]]),
        # Same start, different ends
        ([[1, 4], [1, 5]], [[1, 5]]),
        # Same end, different starts
        ([[2, 5], [1, 5]], [[1, 5]]),
    ],
)
def test_merge_intervals(intervals, expected):
    sol = Solution()
    assert sol.merge(intervals) == expected
