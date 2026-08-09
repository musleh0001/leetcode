import pytest

from problems.array_string.remove_duplicates_from_sorted_array import Solution


@pytest.mark.parametrize(
    "nums, expected_k, expected_elements",
    [
        # Standard Example 1
        ([1, 1, 2], 2, [1, 2]),
        # Standard Example 2
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        # Empty array
        ([], 0, []),
        # Single element
        ([1], 1, [1]),
        # All elements identical
        ([2, 2, 2, 2, 2], 1, [2]),
        # Already unique array
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        # Negative numbers
        ([-3, -3, -2, -1, -1, 0], 4, [-3, -2, -1, 0]),
        # Two elements - duplicates
        ([5, 5], 1, [5]),
        # Two elements - unique
        ([5, 6], 2, [5, 6]),
        # Duplicates with zero and negatives
        ([-10, -10, -10, 0, 10, 10], 3, [-10, 0, 10]),
        # Sequence of pairs
        ([1, 1, 2, 2, 3, 3, 4, 4], 4, [1, 2, 3, 4]),
        # All negative identical
        ([-5, -5, -5], 1, [-5]),
    ],
)
def test_remove_duplicates(nums, expected_k, expected_elements):
    sol = Solution()
    nums_copy = list(nums)
    k = sol.removeDuplicates(nums_copy)
    assert k == expected_k
    assert nums_copy[:k] == expected_elements
