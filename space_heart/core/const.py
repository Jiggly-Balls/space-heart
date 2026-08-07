from __future__ import annotations

import pathlib
import random
from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

__all__ = (
    "DIR_ROOT",
    "DIR_SHADERS",
    "DIR_SHADERS_FRAG",
    "DIR_SHADERS_VERT",
    "FPS",
    "GAME_TITLE",
    "WINDOW_HEIGHT",
    "WINDOW_WIDTH",
    "Colour",
    "ShaderEnum",
)

GAME_TITLE: str = "Space Heart"
WINDOW_WIDTH: int = 960
WINDOW_HEIGHT: int = 540
FPS: float = 120.0

SPACE_LAYERS: int = 8
SPACE_DRAG: float = 0.98

DIR_ROOT: Path = pathlib.Path(__file__).resolve().parent.parent
DIR_SHADERS: Path = DIR_ROOT / "shaders"
DIR_SHADERS_VERT: Path = DIR_SHADERS / "vertex"
DIR_SHADERS_FRAG: Path = DIR_SHADERS / "fragment"


class Colour(Enum):
    ORANGE = (251, 84, 43)
    RED = (255, 51, 81)
    BLUE = (104, 200, 255)
    TEAL = (52, 255, 206)
    LIGHT_GREEN = (46, 255, 78)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    @staticmethod
    def rand_star_colour() -> Colour:
        return random.choice(
            (
                Colour.ORANGE,
                Colour.BLUE,
                Colour.TEAL,
                Colour.WHITE,
            )
        )


@dataclass(slots=True, frozen=True)
class _ShaderData:
    fragment: str | None
    vertex: str


class ShaderEnum(Enum):
    QUAD = _ShaderData("quad.frag", "quad.vert")
