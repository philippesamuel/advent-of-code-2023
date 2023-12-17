"""Parser"""
from day02.game import Color, CubeSet, Game


def parse_game(game: str) -> Game:
    """Parse game from string."""
    id_, cube_sets = game.split(":")
    return Game(id=int(id_.split()[1]), cube_sets=parse_cube_sets(cube_sets))


def parse_cube_sets(cube_sets: str) -> list[CubeSet]:
    """Parse cube sets from string."""
    return [parse_cube_set(cube_set) for cube_set in cube_sets.split(";")]


def parse_cube_set(cube_set: str) -> CubeSet:
    """Parse cube set from string."""
    return {
        Color(color): int(count)
        for color, count in [cube.split() for cube in cube_set.split(",")]
    }
