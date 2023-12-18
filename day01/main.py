"""Day 1 puzzle of Advent of Code 2023

- Read a file. 
- For each line find the first and last digit, forming a two-digits number.
- Calculate the sum of all numbers.

"""
from typing import Iterable

from lib.file_io import read_lines
from lib.stringslib import find_number


def main() -> None:
    # read file yielding each line
    file_path: str = "./data/day01_input.txt"
    lines: Iterable[str] = read_lines(file_path)
    # for line in lines:
    #    print(line.strip())
    #    print(find_number(line))
    sum_of_numbers = sum(map(find_number, lines))
    print(sum_of_numbers)


if __name__ == "__main__":
    main()
