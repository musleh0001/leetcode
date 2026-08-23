import pytest

from problems.hashmap.contains_duplicate import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Standard Example 1
        ([1, 2, 3, 1], True),
        # Standard Example 2
        ([1, 2, 3, 4], False),
        # Standard Example 3
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        # Single element
        ([1], False),
        # Two elements - distinct
        ([1, 2], False),
        # Two elements - duplicate
        ([5, 5], True),
        # Negative numbers - distinct
        ([-5, -4, -3, -2, -1], False),
        # Negative numbers - duplicate
        ([-1, -2, -3, -1], True),
        # Mixed positive, negative, and zero - duplicate
        ([-10, 5, 0, 10, -10], True),
        # All identical elements
        ([0, 0, 0, 0], True),
        # Duplicates at boundaries
        ([7, 1, 2, 3, 4, 7], True),
        # Large distinct array
        (list(range(100)), False),
        # Large array with duplicate
        (list(range(100)) + [42], True),
    ],
)
def test_contains_duplicate(nums, expected):
    sol = Solution()
    assert sol.containsDuplicate(nums) == expected
