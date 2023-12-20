"""Day 3 puzzle of Advent of Code 2023"""
import itertools
import re
from typing import Iterable, Iterator, TypeAlias, TypeVar

T = TypeVar("T")
Triplet: TypeAlias = tuple[T, T, T]
StrTriplet = Triplet[str]
NUMBER_PATTERN = re.compile(r"\d+")
SYMBOLS = ["#", "$", "%", "&", "*", "+", "-", "/", "=", "@"]
SYMBOL_PATTERN = re.compile(r"\D")
# SYMBOL_PATTERN = re.compile(r"(?!\n|\.|\d|\s)")


def main() -> None:
    file_path: str = "./data/day03_input.txt"
    row_triplets: Iterable[StrTriplet] = read_row_triplets(file_path)
    numbers = map(find_numbers_with_adjacent_symbol, row_triplets)
    # for i, n in enumerate(numbers):
    # print(i+1, n)
    print(sum(itertools.chain(*numbers)))


def read_row_triplets(file_path: str) -> Iterator[StrTriplet]:
    """Read a file and return a tuple of three lines at a time."""
    with open(file_path, "rt", encoding="utf-8") as f:
        f_extended = itertools.chain([""], f, [""])
        yield from tripletwise(f_extended)


def tripletwise(iterable: Iterable[T]) -> Iterator[tuple[T, T, T]]:
    """s -> (s0,s1,s2), (s1,s2,s3), (s2,s3,s4), ..."""
    a, b, c = itertools.tee(iterable, 3)
    next(c, None)
    next(c, None)
    next(b, None)
    return zip(a, b, c)


def find_numbers_with_adjacent_symbol(row_triplet: StrTriplet) -> list[int]:
    """Find numbers in the center row that have a symbol adjacent to them."""
    numbers = find_numbers(row_triplet[1])
    return [
        int(n.group()) for n in numbers if has_adjacent_symbol(n.span(), row_triplet)
    ]


def find_numbers(row: str) -> Iterator[re.Match]:
    """Find numbers in a row."""
    return NUMBER_PATTERN.finditer(row)


def has_adjacent_symbol(span: tuple[int, int], row_triplet: StrTriplet) -> bool:
    """Check if a number has a symbol adjacent to it."""
    (
        left,
        right,
    ) = span
    (
        previous_row,
        current_row,
        next_row,
    ) = row_triplet
    if left == 0:
        adjacent_cells = "".join(
            (
                *previous_row[: right + 1],
                current_row[right],
                *next_row[: right + 1],
            )
        )
    elif right == 140:
        adjacent_cells = "".join(
            (
                *previous_row[left - 1 :],
                current_row[left - 1],
                *next_row[left - 1 :],
            )
        )
    else:
        adjacent_cells = "".join(
            (
                *previous_row[left - 1 : right + 1],
                current_row[left - 1],
                current_row[right],
                *next_row[left - 1 : right + 1],
            )
        )

    return has_symbol(adjacent_cells)


def has_symbol(cells: str) -> bool:
    """Check if any of the cells contain a symbol."""
    clean_cells = cells.replace(".", "").replace("\n", "")
    if SYMBOL_PATTERN.search(clean_cells):
        # print(repr(clean_cells))
        return True
    # print(repr(clean_cells))
    # if any(symbol in cells for symbol in SYMBOLS):
    #     return True
    return False


if __name__ == "__main__":
    main()
