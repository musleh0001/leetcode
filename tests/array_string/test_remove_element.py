import pytest

from problems.array_string.remove_element import Solution


@pytest.mark.parametrize(
    "nums, val, expected_k, expected_elements",
    [
        # Standard Example 1
        ([3, 2, 2, 3], 3, 2, [2, 2]),
        # Standard Example 2
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 0, 1, 3, 4]),
        # Empty array
        ([], 1, 0, []),
        # No elements equal to val
        ([1, 2, 3, 4], 5, 4, [1, 2, 3, 4]),
        # All elements equal to val
        ([7, 7, 7, 7], 7, 0, []),
        # Single element matching val
        ([1], 1, 0, []),
        # Single element not matching val
        ([1], 2, 1, [1]),
        # Negative numbers
        ([-1, -2, -1, 3], -1, 2, [-2, 3]),
        # Alternating elements
        ([1, 2, 1, 2, 1, 2], 1, 3, [2, 2, 2]),
        # val = 0 with zeroes
        ([0, 0, 1, 0, 2], 0, 2, [1, 2]),
        # Repeated values
        ([4, 5, 4, 5, 4, 5, 4], 4, 3, [5, 5, 5]),
        # All negative values
        ([-5, -5, -3, -2], -5, 2, [-3, -2]),
    ],
)
def test_remove_element(nums, val, expected_k, expected_elements):
    sol = Solution()
    nums_copy = list(nums)
    k = sol.removeElement(nums_copy, val)
    assert k == expected_k
    assert sorted(nums_copy[:k]) == sorted(expected_elements)
