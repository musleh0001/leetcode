import pytest

from problems.hashmap.longest_consecutive_sequence import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Standard Example 1
        ([100, 4, 200, 1, 3, 2], 4),
        # Standard Example 2
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        # Empty array
        ([], 0),
        # Single element
        ([1], 1),
        # Two consecutive elements
        ([1, 2], 2),
        # Two non-consecutive elements
        ([1, 3], 1),
        # All duplicate elements
        ([5, 5, 5, 5, 5], 1),
        # Duplicates within consecutive sequence
        ([1, 2, 0, 1], 3),
        # Negative numbers consecutive sequence
        ([-5, -4, -3, -2, -1], 5),
        # Negative and positive numbers crossing zero
        ([-2, -1, 0, 1, 2], 5),
        # Multiple disjoint sequences of different lengths
        ([10, 11, 12, 1, 2, 20, 21, 22, 23], 4),
        # All non-consecutive spaced numbers
        ([10, 30, 50, 70], 1),
        # Large boundary values
        ([-1000000000, 1000000000, 0], 1),
    ],
)
def test_longest_consecutive(nums, expected):
    sol = Solution()
    assert sol.longestConsecutive(nums) == expected
