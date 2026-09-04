import pytest

from problems.array_string.product_of_array_except_self import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Standard Example 1
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        # Standard Example 2 (single zero)
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        # Two zeros (all products are zero)
        ([0, 0], [0, 0]),
        # Multiple zeros with other non-zeros
        ([1, 2, 0, 4, 0], [0, 0, 0, 0, 0]),
        # Minimal length array (two positive elements)
        ([5, 10], [10, 5]),
        # Two negative elements
        ([-2, -3], [-3, -2]),
        # Mixed positive and negative numbers
        ([-1, 2, -3, 4], [-24, 12, -8, 6]),
        # All ones
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        # All negative ones (odd length)
        ([-1, -1, -1], [1, 1, 1]),
        # All negative ones (even length)
        ([-1, -1, -1, -1], [-1, -1, -1, -1]),
        # Zero at the beginning
        ([0, 4, 5], [20, 0, 0]),
        # Zero at the end
        ([4, 5, 0], [0, 0, 20]),
        # Distinct factors with mixed signs
        ([2, 3, -4, 5], [-60, -40, 30, -24]),
    ],
)
def test_product_except_self(nums, expected):
    sol = Solution()
    assert sol.productExceptSelf(nums) == expected
