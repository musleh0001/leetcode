from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional["ListNode"] = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a linked list, return the node where the cycle begins.
        If there is no cycle, return None.

        There is a cycle in a linked list if there is some node in the list that can be reached
        again by continuously following the next pointer. Internally, pos is used to denote the
        index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there
        is no cycle. Note that pos is not passed as a parameter.

        Do not modify the linked list.
        """

        slow = fast = head

        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next

            if slow == fast:
                ptr1 = head
                ptr2 = slow

                while ptr1 != ptr2:
                    ptr1 = ptr1.next  # type: ignore
                    ptr2 = ptr2.next
                return ptr1
        return
