class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Given a string s consisting of words and spaces, return the length of the last word in the string.

        A word is a maximal substring consisting of non-space characters only.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        i = len(s) - 1
        length = 0

        while i >= 0 and s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length

        # return len(s.strip().split()[-1])
