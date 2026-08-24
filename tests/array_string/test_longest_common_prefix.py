import pytest

from problems.array_string.longest_common_prefix import Solution


@pytest.mark.parametrize(
    "strs, expected",
    [
        # Standard Example 1
        (["flower", "flow", "flight"], "fl"),
        # Standard Example 2
        (["dog", "racecar", "car"], ""),
        # Single string
        (["alone"], "alone"),
        # Contains an empty string
        (["", "b"], ""),
        # All empty strings
        (["", "", ""], ""),
        # Identical strings
        (["interspecies", "interspecies", "interspecies"], "interspecies"),
        # Prefix is the entire shortest string
        (["ab", "a"], "a"),
        # Shortest string at the beginning
        (["a", "ab", "abc"], "a"),
        # Single character common prefix
        (["cir", "car"], "c"),
        # Disjoint first characters
        (["a", "b", "c"], ""),
        # Two identical strings
        (["code", "code"], "code"),
        # Longer common prefix
        (["reflower", "reflow", "reflection"], "refl"),
    ],
)
def test_longest_common_prefix(strs, expected):
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == expected
