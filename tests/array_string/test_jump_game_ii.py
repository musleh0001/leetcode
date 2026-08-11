import pytest

from problems.array_string.jump_game_ii import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Standard Example 1
        ([2, 3, 1, 1, 4], 2),
        # Standard Example 2
        ([2, 3, 0, 1, 4], 2),
        # Single element zero (already at last index)
        ([0], 0),
        # Single element positive
        ([10], 0),
        # Two elements
        ([1, 2], 1),
        # Two elements with large jump
        ([5, 1], 1),
        # Direct big jump from start
        ([5, 1, 1, 1, 1, 1], 1),
        # All ones (step by step)
        ([1, 1, 1, 1], 3),
        # Choosing optimal next reach
        ([1, 2, 1, 1, 1], 3),
        # Long array with large jumps
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0], 2),
        # Jump landing exactly on last element
        ([2, 1, 1, 1], 2),
        # Zero in middle not reached due to jump choices
        ([3, 4, 0, 1, 1], 2),
    ],
)
def test_jump(nums, expected):
    sol = Solution()
    assert sol.jump(nums) == expected
