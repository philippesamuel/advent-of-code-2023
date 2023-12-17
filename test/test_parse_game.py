from day02.game import Game, Color
from day02.parser import parse_game


def test_parse_game() -> None:
    """Test parse_game."""
    input_ = "Game 1: 2 blue, 4 green; 7 blue, 1 red, 14 green; 5 blue, 13 green, 1 red; 1 red, 7 blue, 11 green"
    output = Game(
        id=1,
        cube_sets=[
            {Color.BLUE: 2, Color.GREEN: 4},
            {Color.BLUE: 7, Color.RED: 1, Color.GREEN: 14},
            {Color.BLUE: 5, Color.GREEN: 13, Color.RED: 1},
            {Color.RED: 1, Color.BLUE: 7, Color.GREEN: 11},
        ],
    )

    assert parse_game(input_) == output
