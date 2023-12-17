"""Game model."""
from enum import Enum
from pydantic import BaseModel


class Color(str, Enum):
    """Color enum."""
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


CubeSet = dict[Color, int]


class Game(BaseModel):
    """Game model."""
    id: int
    cube_sets: list[CubeSet]
