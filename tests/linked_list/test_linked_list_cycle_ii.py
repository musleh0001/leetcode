from typing import Optional

import pytest

from problems.linked_list.linked_list_cycle_ii import ListNode, Solution


def create_linked_list_with_cycle(
    values: list[int], pos: int
) -> tuple[Optional[ListNode], Optional[ListNode]]:
    if not values:
        return None, None

    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    expected_node = None
    if 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]
        expected_node = nodes[pos]

    return nodes[0], expected_node


@pytest.mark.parametrize(
    "values, pos",
    [
        # Standard Example 1: cycle connects to index 1
        ([3, 2, 0, -4], 1),
        # Standard Example 2: cycle connects to index 0 (head)
        ([1, 2], 0),
        # Standard Example 3: single node, no cycle
        ([1], -1),
        # Empty input list
        ([], -1),
        # Single element with cycle (self-loop)
        ([1], 0),
        # Two elements without cycle
        ([1, 2], -1),
        # Longer list without cycle
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1),
        # Cycle pointing to head (pos = 0)
        ([1, 2, 3, 4, 5], 0),
        # Cycle pointing to middle (pos = 2)
        ([1, 2, 3, 4, 5], 2),
        # Cycle pointing to tail itself (pos = 4)
        ([1, 2, 3, 4, 5], 4),
        # Cycle pointing to penultimate node (pos = 3)
        ([10, 20, 30, 40, 50], 3),
        # Negative numbers with cycle
        ([-10, -20, -30, -40], 1),
        # Negative numbers without cycle
        ([-5, -4, -3, -2, -1], -1),
        # Duplicates with cycle
        ([1, 1, 1, 1], 1),
        # All zeros without cycle
        ([0, 0, 0], -1),
        # Boundary / Extreme values with cycle
        ([-100000, 100000], 0),
    ],
)
def test_linked_list_cycle_ii(values, pos):
    head, expected_node = create_linked_list_with_cycle(values, pos)
    sol = Solution()
    assert sol.detectCycle(head) is expected_node
