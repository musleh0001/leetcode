import pytest

from problems.array_string.majority_element import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Standard Example 1
        ([3, 2, 3], 3),
        # Standard Example 2
        ([2, 2, 1, 1, 1, 2, 2], 2),
        # Single element
        ([1], 1),
        # Two identical elements
        ([5, 5], 5),
        # Three identical elements
        ([7, 7, 7], 7),
        # All negative numbers
        ([-1, -1, -2, -1], -1),
        # Majority at start
        ([10, 10, 10, 1, 2], 10),
        # Majority at end
        ([1, 2, 99, 99, 99], 99),
        # Interleaved majority
        ([4, 1, 4, 2, 4], 4),
        # Large array
        ([6] * 100 + [1] * 49, 6),
        # Zero as majority
        ([0, 0, 0, 1, 0], 0),
        # Negative and positive mix
        ([-5, 3, -5, -5, 2], -5),
    ],
)
def test_majority_element(nums, expected):
    sol = Solution()
    assert sol.majorityElement(nums) == expected
