from __future__ import annotations

import random
from enum import Enum

__all__ = ("FPS", "GAME_TITLE", "WINDOW_HEIGHT", "WINDOW_WIDTH", "Colour")

GAME_TITLE: str = "Space Heart"
WINDOW_WIDTH: int = 960
WINDOW_HEIGHT: int = 540
FPS: float = 120.0

SPACE_LAYERS: int = 10
SPACE_DRAG: float = 0.98


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
