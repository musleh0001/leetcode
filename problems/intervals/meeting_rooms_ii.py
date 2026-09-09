import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Given an array of meeting time intervals where intervals[i] = [start_i, end_i],
        return the minimum number of conference rooms required.
        """

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if free_rooms[0] <= start:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, end)

        return len(free_rooms)
