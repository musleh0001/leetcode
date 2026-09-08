from typing import Optional

import pytest

from problems.linked_list.linked_list_cycle import ListNode, Solution


def create_linked_list(values: list[int], pos: int) -> Optional[ListNode]:
    if not values:
        return None

    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]

    return nodes[0]


@pytest.mark.parametrize(
    "values, pos, expected",
    [
        # Standard Example 1
        ([3, 2, 0, -4], 1, True),
        # Standard Example 2
        ([1, 2], 0, True),
        # Standard Example 3
        ([1], -1, False),
        # Empty input list
        ([], -1, False),
        # Single element with cycle (self-loop)
        ([1], 0, True),
        # Two elements without cycle
        ([1, 2], -1, False),
        # Longer list without cycle
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1, False),
        # Cycle pointing to head (pos = 0)
        ([1, 2, 3, 4, 5], 0, True),
        # Cycle pointing to middle (pos = 2)
        ([1, 2, 3, 4, 5], 2, True),
        # Cycle pointing to tail itself (pos = 4)
        ([1, 2, 3, 4, 5], 4, True),
        # Negative numbers with cycle
        ([-10, -20, -30, -40], 1, True),
        # Negative numbers without cycle
        ([-5, -4, -3, -2, -1], -1, False),
        # Duplicates with cycle
        ([1, 1, 1, 1], 0, True),
        # All zeros without cycle
        ([0, 0, 0], -1, False),
        # Boundary / Extreme values with cycle
        ([-100000, 100000], 0, True),
    ],
)
def test_linked_list_cycle(values, pos, expected):
    head = create_linked_list(values, pos)
    sol = Solution()
    assert sol.hasCycle(head) == expected
