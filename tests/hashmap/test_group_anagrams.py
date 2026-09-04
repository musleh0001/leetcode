import pytest

from problems.hashmap.group_anagrams import Solution


@pytest.mark.parametrize(
    "strs, expected",
    [
        # Standard Example 1
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        # Standard Example 2 (single empty string)
        ([""], [[""]]),
        # Standard Example 3 (single character string)
        (["a"], [["a"]]),
        # Multiple empty strings
        (["", ""], [["", ""]]),
        # No anagrams (all distinct words)
        (["a", "b", "c", "d"], [["a"], ["b"], ["c"], ["d"]]),
        # All words are anagrams of each other
        (
            ["abc", "bca", "cab", "cba", "bac", "acb"],
            [["abc", "acb", "bac", "bca", "cab", "cba"]],
        ),
        # Duplicate identical words
        (["apple", "banana", "apple"], [["apple", "apple"], ["banana"]]),
        # Words with overlapping character counts
        (["boo", "bob", "obo", "oob"], [["bob"], ["boo", "obo", "oob"]]),
        # Empty strings mixed with non-empty strings
        (["", "b", ""], [["", ""], ["b"]]),
        # Two-word anagram pair
        (["ab", "ba"], [["ab", "ba"]]),
        # Two-word non-anagram pair
        (["ab", "cd"], [["ab"], ["cd"]]),
        # Words of varying lengths across multiple groups
        (
            ["listen", "silent", "enlist", "google", "gogole", "banana"],
            [
                ["listen", "silent", "enlist"],
                ["google", "gogole"],
                ["banana"],
            ],
        ),
        # Single characters with duplicates
        (["a", "a", "b", "b", "c"], [["a", "a"], ["b", "b"], ["c"]]),
    ],
)
def test_group_anagrams(strs, expected):
    sol = Solution()
    result = sol.groupAnagrams(strs)
    assert result is not None
    assert sorted([sorted(g) for g in result]) == sorted([sorted(g) for g in expected])
