from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i]
        represent the start and the end of the ith interval and intervals is sorted in ascending order by start_i.
        You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

        Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and
        intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

        Return intervals after the insertion.
        """

        res = []
        i = 0
        n = len(intervals)

        # Phase 1: Add all intervals ending before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Phase 2: Merge all overlapping intervals into newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # Phase 3: Add all remaining intervals after newInterval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
