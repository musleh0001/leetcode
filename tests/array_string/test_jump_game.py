import pytest

from problems.array_string.jump_game import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Standard Example 1
        ([2, 3, 1, 1, 4], True),
        # Standard Example 2
        ([3, 2, 1, 0, 4], False),
        # Single element zero (already at last index)
        ([0], True),
        # Single element positive
        ([5], True),
        # Two elements - can reach
        ([1, 0], True),
        # Two elements - cannot reach
        ([0, 1], False),
        # Can reach end despite zeros
        ([2, 0, 0], True),
        # Zero trapped before end
        ([1, 0, 0], False),
        # Jumps over zero successfully
        ([2, 0, 1, 0], True),
        # Large jump from start
        ([5, 0, 0, 0, 0], True),
        # All ones
        ([1, 1, 1, 1, 1], True),
        # Start with zero but multiple elements
        ([0, 2, 3], False),
        # Failed multi-step jump
        ([1, 2, 0, 1, 0, 1], False),
    ],
)
def test_can_jump(nums, expected):
    sol = Solution()
    assert sol.canJump(nums) == expected
