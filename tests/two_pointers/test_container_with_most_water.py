import pytest

from problems.two_pointers.container_with_most_water import Solution


@pytest.mark.parametrize(
    "height, expected",
    [
        # Standard Example 1
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        # Standard Example 2 (minimal length, identical heights)
        ([1, 1], 1),
        # Minimal length with unequal heights
        ([4, 3], 3),
        # Strictly increasing heights
        ([1, 2, 3, 4, 5], 6),
        # Strictly decreasing heights
        ([5, 4, 3, 2, 1], 6),
        # Tall pillars at the extreme boundaries
        ([10, 1, 1, 1, 1, 10], 50),
        # Tall pillars adjacent in the middle
        ([1, 100, 100, 1], 100),
        # All identical elements
        ([5, 5, 5, 5, 5], 20),
        # Array with zero heights
        ([0, 2, 0], 0),
        # Zeroes at edges with positive values inside
        ([0, 5, 4, 0], 4),
        # Plateau with large values adjacent
        ([2, 3, 4, 5, 18, 17, 6], 17),
        # Fluctuating heights
        ([1, 2, 4, 3], 4),
        # Maximum constraint boundary values
        ([10000, 10000], 10000),
    ],
)
def test_container_with_most_water(height, expected):
    sol = Solution()
    assert sol.maxArea(height) == expected
