import pytest

from problems.arrays.find_closest_number_to_zero import Solution


# use parametrize to test multiple cases
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 1, 1, 3], 1),
        ([2, -1, 1], 1),
        ([-2, -1, 1, 2], 1),
        ([1], 1),
        ([-1], -1),
        ([0], 0),
        ([0, 1, 2], 0),
        ([-4, -2, 1, 4, 8], 1),
    ],
)
def test_find_closest_number_to_zero(nums, expected):
    result = Solution().findClosestNumber(nums)
    assert result == expected
