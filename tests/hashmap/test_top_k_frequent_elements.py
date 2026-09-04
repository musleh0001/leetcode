import pytest

from problems.hashmap.top_k_frequent_elements import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        # Standard Example 1
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        # Standard Example 2 (single element, k = 1)
        ([1], 1, [1]),
        # Multiple elements with same top frequencies
        ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),
        # All negative numbers
        ([-1, -1, -2, -2, -2, -3], 2, [-2, -1]),
        # All identical elements
        ([7, 7, 7, 7, 7], 1, [7]),
        # Distinct frequency counts for each element
        ([10, 10, 10, 10, 20, 20, 20, 30, 30, 40], 3, [10, 20, 30]),
        # k equals total number of unique elements
        ([1, 2, 3], 3, [1, 2, 3]),
        # Array containing zeros
        ([0, 0, 0, 1, 2], 1, [0]),
        # Large boundary values
        ([-10000, -10000, 10000, 10000, 10000, 0], 2, [-10000, 10000]),
        # Small array with duplicate majority
        ([1, 2, 2], 1, [2]),
        # Dominant frequency majority
        ([5] * 100 + [1, 2, 3], 1, [5]),
        # Alternating sequence
        ([1, 2, 1, 2, 1, 3, 1], 1, [1]),
        # Minimal length with k = 2
        ([1, 2], 2, [1, 2]),
    ],
)
def test_top_k_frequent(nums, k, expected):
    sol = Solution()
    result = sol.topKFrequent(nums, k)
    assert result is not None
    assert sorted(result) == sorted(expected)
