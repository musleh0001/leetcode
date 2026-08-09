import pytest
from problems.array_string.remove_duplicates_from_sorted_array_ii import Solution


@pytest.mark.parametrize(
    "nums, expected_k, expected_elements",
    [
        # Standard Example 1
        ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
        # Standard Example 2
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
        # Empty array
        ([], 0, []),
        # Single element
        ([1], 1, [1]),
        # Two identical elements
        ([1, 1], 2, [1, 1]),
        # Three identical elements
        ([1, 1, 1], 2, [1, 1]),
        # All elements identical (5 elements)
        ([2, 2, 2, 2, 2], 2, [2, 2]),
        # Already valid with max 2 duplicates
        ([1, 1, 2, 2, 3, 3], 6, [1, 1, 2, 2, 3, 3]),
        # Already unique elements
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
        # Negative numbers with triple duplicates
        ([-3, -3, -3, -1, -1, 0, 0, 0], 6, [-3, -3, -1, -1, 0, 0]),
        # Large duplicate streaks
        ([1, 1, 1, 1, 1, 1, 2, 2, 2, 2], 4, [1, 1, 2, 2]),
        # Alternating frequencies
        ([-5, -5, -4, -3, -3, -3], 5, [-5, -5, -4, -3, -3]),
    ],
)
def test_remove_duplicates_ii(nums, expected_k, expected_elements):
    sol = Solution()
    nums_copy = list(nums)
    k = sol.removeDuplicates(nums_copy)
    assert k == expected_k
    assert nums_copy[:k] == expected_elements
