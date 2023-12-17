"""Functions for string manipulation."""
from functools import partial
from typing import Callable
from lib.typings import MaybeInt

DIGITS = list("123456789")
DIGIT_CHARACTER2NAME_MAP = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}


def find_number(line: str) -> int:
    """Find the first and last digit in a string and return the number formed by these two digits"""
    first: int = find_first_digit(line)
    last: int = find_last_digit(line)
    return first * 10 + last


def find_digit(
    line: str,
    get_digit_index_method: Callable[[str, str], int],
    minmax_method: Callable,
) -> MaybeInt:
    """Return the first digit in a string."""
    digit_indices = {}
    for digit in DIGITS:
        index = get_digit_index_method(digit, line)
        if index is not None:
            digit_indices[digit] = index
    if digit_indices:
        return int(minmax_method(digit_indices, key=digit_indices.get))
    return None


def get_digit_index(
    digit: str,
    line: str,
    find_method: Callable[[str, str], int] = str.find,
    minmax_method: Callable[[int, int], int] = min,
) -> MaybeInt:
    """Return the index of the first occurrence of a digit in a string."""
    digit_name = DIGIT_CHARACTER2NAME_MAP[digit]
    digit_index = find_method(line, digit)
    digit_name_index = find_method(line, digit_name)
    if (digit_index >= 0) and (digit_name_index >= 0):
        return minmax_method(digit_index, digit_name_index)
    if digit_name_index >= 0:
        return digit_name_index
    if digit_index >= 0:
        return digit_index
    return None


get_first_occurrence_digit_index = get_digit_index
get_last_occurrence_digit_index = partial(
    get_digit_index, find_method=str.rfind, minmax_method=max
)

find_first_digit = partial(
    find_digit,
    get_digit_index_method=get_first_occurrence_digit_index,
    minmax_method=min,
)
find_last_digit = partial(
    find_digit,
    get_digit_index_method=get_last_occurrence_digit_index,
    minmax_method=max,
)
