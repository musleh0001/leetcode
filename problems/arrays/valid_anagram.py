class Solution:
    """
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    """

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26  # For lowercase English letters

        for char in s:
            count[ord(char) - ord("a")] += 1

        for char in t:
            count[ord(char) - ord("a")] -= 1
            if count[ord(char) - ord("a")] < 0:
                return False

        return True

    def isAnagram_v2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
