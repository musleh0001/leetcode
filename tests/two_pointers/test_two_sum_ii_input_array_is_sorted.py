import pytest

from problems.two_pointers.two_sum_ii_input_array_is_sorted import Solution


@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        # Standard Example 1
        ([2, 7, 11, 15], 9, [1, 2]),
        # Standard Example 2
        ([2, 3, 4], 6, [1, 3]),
        # Standard Example 3
        ([-1, 0], -1, [1, 2]),
        # Two zeros summing to zero
        ([0, 0, 3, 4], 0, [1, 2]),
        # Duplicate positive numbers forming target
        ([1, 2, 3, 4, 4, 9, 10], 8, [4, 5]),
        # All negative numbers
        ([-5, -3, -2, -1], -8, [1, 2]),
        # Mixed negative and positive summing to zero
        ([-10, -3, 0, 2, 4, 10], 0, [1, 6]),
        # Minimal array length (two elements)
        ([1, 2], 3, [1, 2]),
        # First and last elements (extreme boundaries)
        ([1, 2, 3, 4, 5, 6, 100], 101, [1, 7]),
        # Adjacent elements in the middle
        ([1, 3, 5, 6, 11, 15], 11, [3, 4]),
        # Negative target with mixed numbers
        ([-7, -2, 1, 3, 8], -9, [1, 2]),
        # Large boundary values
        ([-1000, -500, 0, 500, 1000], 0, [1, 5]),
    ],
)
def test_two_sum(numbers, target, expected):
    sol = Solution()
    assert sol.twoSum(numbers, target) == expected
