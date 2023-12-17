"""Day 2 puzzle of Advent of Code 2023."""
import json
from typing import Iterable, Iterator
from day02.game import Game, Color, CubeSet
from day02.parser import parse_game

CONSTRAINTS = {Color.RED: 12, Color.GREEN: 13, Color.BLUE: 14}


def main():
    """Day 2 puzzle of Advent of Code 2023"""
    file_path: str = "./data/day02_input.txt"
    games: Iterable[Game] = read_and_parse_games(file_path)
    possible_games = filter(is_game_possible, games)
    print(sum(g.id for g in possible_games))


def read_games_json(file_path: str) -> Iterator[Game]:
    """Read games from json file."""
    with open(file_path, "rt", encoding="utf-8") as f:
        for game in json.load(f):
            yield Game(**game)


def read_and_parse_games(file_path: str) -> Iterator[Game]:
    """Read and parse games from file."""
    with open(file_path, "rt", encoding="utf-8") as f:
        for game in f:
            yield parse_game(game)


def is_game_possible(game: Game) -> bool:
    """Check if the game is possible, according to CONSTRAINTS."""
    return all(map(is_cube_set_possible, game.cube_sets))


def is_cube_set_possible(cube_set: CubeSet) -> bool:
    """Check if the cube set is possible, according to CONSTRAINTS."""
    return all(
        cube_set.get(color, 0) <= constraint
        for color, constraint in CONSTRAINTS.items()
    )


if __name__ == "__main__":
    main()
