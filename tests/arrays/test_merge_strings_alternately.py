import pytest

from problems.arrays.merge_strings_alternately import Solution


@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        # Equal length strings
        ("abc", "def", "adbecf"),
        # word1 is longer
        ("abcd", "ef", "aebfcd"),
        # word2 is longer
        ("ab", "cdef", "acbdef"),
        # Empty strings
        ("", "", ""),
        # One empty string
        ("abc", "", "abc"),
        ("", "def", "def"),
        # Single character strings
        ("a", "b", "ab"),
        # Longer strings
        ("hello", "world", "hweolrllod"),
        # Repeated characters
        ("aaa", "bbb", "ababab"),
    ],
)
def test_merge_alternately(word1, word2, expected):
    assert Solution().mergeAlternately(word1, word2) == expected
