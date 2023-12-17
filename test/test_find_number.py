"""Test find_number function."""
from functools import partial
import pytest
from day01.main import find_number


LINES = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
    "four1dsgpfzltwo57threefivetwo",
    "seven3lbcvjxqhhdpzkttqsixjzzjjbclfq1fiveeightwojx",
    "seightwoone8qxcfgszninesvfcnxc68"
]

EXPECTED = [29, 83, 13, 24, 42, 14, 76, 42, 72, 88]


@pytest.mark.parametrize(["line", "expected"], zip(LINES, EXPECTED))
def test_find_number_with_digit_name(line: str, expected: int) -> None:
    """Test find_number function."""
    result = find_number(line)
    assert result == expected
