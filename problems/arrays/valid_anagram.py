class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(k)
        """

        if len(s) != len(t):
            return False

        # Frequency dict to count char
        count: dict[str, int] = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return True

    def isAnagram_sort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
