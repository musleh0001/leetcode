from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Write a function to find the longest common prefix string amongst an array of strings.

        If there is no common prefix, return an empty string "".

        Time Complexity: O(S) where S is the sum of all characters in all strings
        Space Complexity: O(1)
        """

        if not strs:
            return ""

        for index, char in enumerate(strs[0]):
            for other in strs[1:]:
                if index == len(other) or other[index] != char:
                    return strs[0][:index]

        return strs[0]
