import pytest

from problems.hashmap.valid_anagram import Solution


@pytest.mark.parametrize(
    "s, t, expected",
    [
        # Standard Example 1
        ("anagram", "nagaram", True),
        # Standard Example 2
        ("rat", "car", False),
        # Single char matching
        ("a", "a", True),
        # Single char differing
        ("a", "b", False),
        # Different lengths
        ("a", "ab", False),
        # Different lengths (s longer than t)
        ("hello", "hell", False),
        # Same characters but different frequencies
        ("aacc", "ccac", False),
        # Reversed string anagram
        ("abcde", "edcba", True),
        # Common anagram pair 1
        ("listen", "silent", True),
        # Common anagram pair 2
        ("triangle", "integral", True),
        # All same characters matching
        ("aaaa", "aaaa", True),
        # Same counts of different letters
        ("aabbcc", "bbaacc", True),
        # Completely disjoint characters
        ("abc", "def", False),
    ],
)
def test_valid_anagram(s, t, expected):
    sol = Solution()
    assert sol.isAnagram(s, t) == expected
