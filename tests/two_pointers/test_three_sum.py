import pytest

from problems.two_pointers.three_sum import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Standard Example 1
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        # Standard Example 2 (no triplet sums to zero)
        ([0, 1, 1], []),
        # Standard Example 3 (all zeros, exactly 3)
        ([0, 0, 0], [[0, 0, 0]]),
        # More than three zeros (no duplicate triplets)
        ([0, 0, 0, 0], [[0, 0, 0]]),
        # Duplicate values producing a single valid triplet
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
        # Multiple duplicated elements forming one triplet
        ([-1, -1, -1, 0, 1, 1, 1], [[-1, 0, 1]]),
        # All negative numbers
        ([-5, -4, -3, -2, -1], []),
        # All positive numbers
        ([1, 2, 3, 4, 5], []),
        # Minimal valid triplet length
        ([-2, 1, 1], [[-2, 1, 1]]),
        # Two distinct triplets
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        # Multiple distinct triplets with zero and opposite pairs
        ([-3, -1, 0, 1, 2, 3], [[-3, 0, 3], [-3, 1, 2], [-1, 0, 1]]),
        # Large boundary values
        ([-100000, 0, 100000], [[-100000, 0, 100000]]),
        # Duplicates with single zero-sum
        ([-4, 2, 2], [[-4, 2, 2]]),
    ],
)
def test_three_sum(nums, expected):
    sol = Solution()
    result = sol.threeSum(nums)
    assert result is not None
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])
