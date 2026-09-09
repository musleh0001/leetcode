import pytest

from problems.intervals.meeting_rooms_ii import Solution


@pytest.mark.parametrize(
    "intervals, expected",
    [
        # Standard Example 1
        ([[0, 30], [5, 10], [15, 20]], 2),
        # Standard Example 2
        ([[7, 10], [2, 4]], 1),
        # Empty intervals list
        ([], 0),
        # Single meeting
        ([[1, 5]], 1),
        # Back-to-back meetings touching at boundary (same room reused)
        ([[0, 5], [5, 10], [10, 15]], 1),
        # All meetings overlap concurrently
        ([[1, 10], [2, 9], [3, 8], [4, 7]], 4),
        # Identical meeting times
        ([[2, 6], [2, 6], [2, 6]], 3),
        # Overlap with room reuse
        ([[1, 4], [2, 5], [7, 9], [3, 6]], 3),
        # Unsorted intervals with overlap
        ([[9, 10], [4, 9], [4, 17]], 2),
        # Multiple disjoint meetings with parallel duplicates
        ([[1, 5], [8, 9], [8, 9]], 2),
        # Sequence of disjoint meetings
        ([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], 1),
        # One long meeting spanning multiple back-to-back shorter meetings
        ([[1, 20], [2, 5], [5, 10], [10, 15], [15, 20]], 2),
        # Large boundary values
        ([[0, 1000000], [500000, 1000000]], 2),
        # Meeting ends exactly when another starts while another is active
        ([[1, 10], [2, 7], [7, 9]], 2),
    ],
)
def test_meeting_rooms_ii(intervals, expected):
    sol = Solution()
    assert sol.minMeetingRooms(intervals) == expected
