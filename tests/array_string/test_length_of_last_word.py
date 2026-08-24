import pytest

from problems.array_string.length_of_last_word import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        # Standard Example 1
        ("Hello World", 5),
        # Standard Example 2
        ("   fly me   to   the moon  ", 4),
        # Standard Example 3
        ("luffy is still joyboy", 6),
        # Single word without spaces
        ("hello", 5),
        # Single letter
        ("a", 1),
        # Single letter with surrounding spaces
        ("   a   ", 1),
        # Word with trailing spaces
        ("day   ", 3),
        # Word with leading spaces
        ("   day", 3),
        # Multiple spaces between single-letter words
        ("a   b   c", 1),
        # Long last word
        ("Today is an extraordinaryday", 16),
        # Two single-letter words
        ("a b", 1),
        # Multiple spaces between all words and edges
        ("   lots    of    spaces    here   ", 4),
    ],
)
def test_length_of_last_word(s, expected):
    sol = Solution()
    assert sol.lengthOfLastWord(s) == expected
