import pytest
from problems.array_string.rotate_array import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        # Standard Example 1
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        # Standard Example 2
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        # k = 0 (no rotation)
        ([1, 2, 3], 0, [1, 2, 3]),
        # k equals length
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
        # k greater than length
        ([1, 2], 5, [2, 1]),
        # Single element
        ([1], 10, [1]),
        # Empty array
        ([], 3, []),
        # Two elements, k = 1
        ([1, 2], 1, [2, 1]),
        # Negative numbers
        ([-5, -4, -3, -2, -1], 2, [-2, -1, -5, -4, -3]),
        # Large k multiple of length
        ([10, 20, 30], 300, [10, 20, 30]),
        # k = 1
        ([1, 2, 3, 4, 5], 1, [5, 1, 2, 3, 4]),
        # All identical elements
        ([0, 0, 0], 2, [0, 0, 0]),
    ],
)
def test_rotate(nums, k, expected):
    sol = Solution()
    nums_copy = list(nums)
    sol.rotate(nums_copy, k)
    assert nums_copy == expected
