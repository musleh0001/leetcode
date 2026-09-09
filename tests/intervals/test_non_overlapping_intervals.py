import pytest

from problems.intervals.non_overlapping_intervals import Solution


@pytest.mark.parametrize(
    "intervals, expected",
    [
        # Standard Example 1
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        # Standard Example 2 (identical intervals)
        ([[1, 2], [1, 2], [1, 2]], 2),
        # Standard Example 3 (already non-overlapping)
        ([[1, 2], [2, 3]], 0),
        # Single interval
        ([[1, 2]], 0),
        # Touching boundaries only (non-overlapping)
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 0),
        # Multiple fully overlapping intervals
        ([[1, 10], [2, 9], [3, 8], [4, 7]], 3),
        # Nested intervals where smaller intervals are preserved
        ([[1, 100], [11, 22], [1, 11], [2, 12]], 2),
        # Negative coordinate intervals
        ([[-50, -20], [-30, -10], [-20, 0], [-10, 10]], 2),
        # Mixed negative and positive coordinates without overlap
        ([[-10, -5], [-5, 0], [0, 5], [5, 10]], 0),
        # Unsorted input order
        ([[3, 4], [1, 2], [2, 3]], 0),
        # Long spanning interval overlapping with multiple disjoint sub-intervals
        ([[1, 5], [2, 3], [3, 4], [4, 6]], 1),
        # Four identical intervals
        ([[0, 2], [0, 2], [0, 2], [0, 2]], 3),
        # Alternating chain of overlaps
        ([[1, 3], [2, 4], [3, 5], [4, 6]], 2),
        # Boundary / extreme coordinates
        ([[-50000, 0], [0, 50000]], 0),
    ],
)
def test_non_overlapping_intervals(intervals, expected):
    sol = Solution()
    assert sol.eraseOverlapIntervals(intervals) == expected
