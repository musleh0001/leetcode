import pytest

from problems.arrays.two_sum import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 5, 3, 7], 8, [1, 2]),
        ([0, 4, 3, 0], 0, [0, 3]),
    ],
)
def test_two_sum(nums, target, expected):
    assert Solution().twoSum(nums, target) == expected
