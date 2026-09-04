import heapq
from collections import Counter


class Solution:
    def topKFrequent_v2(self, nums: list[int], k: int) -> list[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements.
        You may return the answer in any order.

        Time Complexity: O(n) or O(n log k)
        Space Complexity: O(n)
        """

        count = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res

        return res

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)  # type: ignore
