import pytest

from problems.intervals.meeting_rooms import Solution


@pytest.mark.parametrize(
    "intervals, expected",
    [
        # Standard Example 1 (overlapping meetings)
        ([[0, 30], [5, 10], [15, 20]], False),
        # Standard Example 2 (non-overlapping, unsorted)
        ([[7, 10], [2, 4]], True),
        # Empty intervals list
        ([], True),
        # Single meeting
        ([[1, 5]], True),
        # Back-to-back meetings touching at boundary
        ([[0, 5], [5, 10], [10, 15]], True),
        # Multiple meetings with two overlapping
        ([[1, 4], [2, 5], [7, 9]], False),
        # Complete overlap / subset
        ([[1, 10], [2, 3]], False),
        # Identical meetings
        ([[1, 5], [1, 5]], False),
        # Sorted non-overlapping meetings
        ([[1, 3], [4, 6], [7, 9], [10, 12]], True),
        # Unsorted non-overlapping meetings
        ([[10, 12], [1, 3], [7, 9], [4, 6]], True),
        # Overlap only between last two meetings
        ([[1, 2], [3, 4], [5, 7], [6, 8]], False),
        # Large boundary values
        ([[0, 500000], [500000, 1000000]], True),
        # Chain of back-to-back unit meetings
        ([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]], True),
        # Slight overlap (starts 1 unit before previous ends)
        ([[1, 5], [4, 8]], False),
    ],
)
def test_meeting_rooms(intervals, expected):
    sol = Solution()
    assert sol.canAttendMeetings(intervals) == expected
