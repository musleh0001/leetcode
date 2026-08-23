class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        if len(s) != len(t):
            return False

        count = [0] * 26

        for char_s, char_t in zip(s, t):
            count[ord(char_s) - ord("a")] += 1
            count[ord(char_t) - ord("a")] -= 1

        return all(c == 0 for c in count)
