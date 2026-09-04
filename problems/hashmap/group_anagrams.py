from collections import defaultdict


class Solution:
    def groupAnagrams_v2(self, strs: list[str]) -> list[list[str]]:
        """
        Given an array of strings strs, group the anagrams together.
        You can return the answer in any order.

        Time Complexity: O(n * k log k) or O(n * k) where k is max length of a string
        Space Complexity: O(n * k)
        """

        anagram_map = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1

            anagram_map[tuple(count)].append(word)

        return list(anagram_map.values())

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_key = "".join(sorted(word))
            anagram_map[sorted_key].append(word)

        return list(anagram_map.values())
