import pytest

from problems.arrays.contains_duplicate import Solution


# use parametrize to test multiple cases
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], False),
        ([1], False),
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 1], True),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([-1, -1], True),
        ([0, 4, 5, 0, 3, 6], True),
    ],
)
def test_contains_duplicate(nums, expected):
    result = Solution().containsDuplicate(nums)
    assert result == expected
