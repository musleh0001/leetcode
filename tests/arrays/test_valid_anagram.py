import pytest

from problems.arrays.valid_anagram import Solution


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "aa", False),
        ("listen", "silent", True),
        ("hello", "billion", False),
        ("aabbcc", "abccba", True),
    ],
)
def test_is_anagram(s, t, expected):
    assert Solution().isAnagram(s, t) == expected
