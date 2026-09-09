from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Given an array of intervals where intervals[i] = [start_i, end_i], return the minimum number
        of intervals you need to remove to make the rest of the intervals non-overlapping.

        Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and
        [2, 3] are non-overlapping.
        """

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < prev_end:
                removals += 1
            else:
                prev_end = end

        return removals
