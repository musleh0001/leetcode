import pytest

from problems.arrays.roman_to_integer import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        # Basic cases
        ("I", 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
        # Simple additions
        ("II", 2),
        ("III", 3),
        ("XX", 20),
        ("XXX", 30),
        ("CC", 200),
        ("MMM", 3000),
        # Subtractive notation
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        # Complex cases
        ("LVIII", 58),  # L = 50, V = 5, III = 3
        ("MCMXCIV", 1994),  # M = 1000, CM = 900, XC = 90, IV = 4
        ("DCXXI", 621),  # D = 500, C = 100, XX = 20, I = 1
        # Edge cases
        ("MMMCMXCIX", 3999),  # Maximum Roman numeral
        ("I", 1),  # Minimum
    ],
)
def test_roman_to_int(s, expected):
    assert Solution().romanToInt(s) == expected
