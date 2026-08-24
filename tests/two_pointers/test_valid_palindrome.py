import pytest

from problems.two_pointers.valid_palindrome import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        # Standard Example 1
        ("A man, a plan, a canal: Panama", True),
        # Standard Example 2
        ("race a car", False),
        # Standard Example 3 (single space)
        (" ", True),
        # Empty string
        ("", True),
        # Non-alphanumeric only
        (".,:;!?", True),
        # Single character
        ("a", True),
        # Two identical characters
        ("aa", True),
        # Two different characters
        ("ab", False),
        # Number and letter (not palindrome)
        ("0P", False),
        # Numbers and letters palindrome
        ("1b1", True),
        # Underscore and letters palindrome
        ("ab_a", True),
        # Mixed case with punctuation
        ("No 'x' in Nixon", True),
        # Another standard palindrome sentence
        ("Was it a car or a cat I saw?", True),
        # Even length palindrome sentence
        ("red rum, sir, is murder", True),
    ],
)
def test_valid_palindrome(s, expected):
    sol = Solution()
    assert sol.isPalindrome(s) == expected
