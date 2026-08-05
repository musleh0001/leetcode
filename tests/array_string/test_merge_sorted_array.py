import pytest

from problems.array_string.merge_sorted_array import Solution


@pytest.mark.parametrize(
    "nums1, m, nums2, n, expected",
    [
        # Standard Example 1
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        # Standard Example 2 (n = 0)
        ([1], 1, [], 0, [1]),
        # Standard Example 3 (m = 0)
        ([0], 0, [1], 1, [1]),
        # m = 0 with multiple elements in nums2
        ([0, 0, 0], 0, [1, 2, 3], 3, [1, 2, 3]),
        # n = 0 with multiple elements in nums1
        ([1, 2, 3], 3, [], 0, [1, 2, 3]),
        # Negative numbers
        ([-5, -3, 0, 0, 0], 2, [-4, -1, 2], 3, [-5, -4, -3, -1, 2]),
        # Duplicates in both arrays
        ([2, 2, 2, 0, 0, 0], 3, [2, 2, 2], 3, [2, 2, 2, 2, 2, 2]),
        # All elements in nums2 are smaller than nums1
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        # All elements in nums1 are smaller than nums2
        ([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3, [1, 2, 3, 4, 5, 6]),
        # Single element in each
        ([2, 0], 1, [1], 1, [1, 2]),
        # Boundary / Extreme values
        ([-1000, 1000, 0, 0], 2, [-500, 500], 2, [-1000, -500, 500, 1000]),
        # Alternating / Interleaved values
        ([1, 3, 5, 7, 0, 0, 0], 4, [2, 4, 6], 3, [1, 2, 3, 4, 5, 6, 7]),
    ],
)
def test_merge_sorted_array(nums1, m, nums2, n, expected):
    sol = Solution()
    nums1_copy = list(nums1)
    sol.merge(nums1_copy, m, nums2, n)
    assert nums1_copy == expected
