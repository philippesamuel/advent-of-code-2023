"""Functions to deal with file I/O."""
from pathlib import Path
from typing import Iterator


def read_lines(file_path: str|Path) -> Iterator[str]:
    """Read a file and yield each line."""
    with open(file=file_path, mode="rt") as f:
        for line in f:
            yield line
            