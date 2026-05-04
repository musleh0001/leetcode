import pytest

from problems.arrays.two_sum import Solution


@pytest.mark.parametrize(
    "nums, target",
    [
        ([3, 3], 6),
        ([0, 4, 3, 0], 0),
        ([1, 2, 3, 1], 2),
        ([2, 2, 3], 4),
        ([5, 5], 10),
    ],
)
def test_two_sum(nums, target):
    res = Solution().twoSum(nums, target)
    # must be a list of two distinct indices
    assert isinstance(res, list)
    assert len(res) == 2
    i, j = res
    assert 0 <= i < len(nums) and 0 <= j < len(nums)
    assert i != j
    assert nums[i] + nums[j] == target
