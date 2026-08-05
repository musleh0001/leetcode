import pytest

from problems.arrays.valid_anagram import Solution


# use parametrize to test multiple cases
@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "ab", False),
        ("ab", "a", False),
        ("a", "a", True),
        ("a", "b", False),
        ("", "", True),
        ("aacc", "ccac", False),
        ("listen", "silent", True),
    ],
)
def test_is_anagram(s, t, expected):
    result = Solution().isAnagram(s, t)
    assert result == expected
