import pytest

from problems.hashmap.two_sum import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        # Standard Example 1
        ([2, 7, 11, 15], 9, [0, 1]),
        # Standard Example 2
        ([3, 2, 4], 6, [1, 2]),
        # Standard Example 3 (duplicate values)
        ([3, 3], 6, [0, 1]),
        # Target with all negative numbers
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        # Mixed positive and negative sum to zero
        ([-3, 4, 3, 90], 0, [0, 2]),
        # Two zeros summing to zero
        ([0, 4, 3, 0], 0, [0, 3]),
        # Zero and non-zero
        ([0, 5, 2, -5], 5, [0, 1]),
        # Boundary elements (first and last)
        ([1, 5, 8, 10, 9], 10, [0, 4]),
        # Large values
        ([1000000000, 3, 500000000, 1000000000], 2000000000, [0, 3]),
        # Minimal array length (two elements)
        ([5, 10], 15, [0, 1]),
        # Adjacent elements in middle
        ([1, 2, 7, 8, 15], 15, [2, 3]),
        # Negative target with positive and negative mix
        ([5, -10, 15, -20], -5, [0, 1]),
    ],
)
def test_two_sum(nums, target, expected):
    sol = Solution()
    result = sol.twoSum(nums, target)
    assert result is not None
    assert sorted(result) == sorted(expected)
