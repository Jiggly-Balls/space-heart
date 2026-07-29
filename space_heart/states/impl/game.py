from __future__ import annotations

import random
from typing import TYPE_CHECKING

import pygame

from space_heart.core.background import SpaceLayer
from space_heart.core.const import WINDOW_HEIGHT, WINDOW_WIDTH
from space_heart.entities.player import Player
from space_heart.states.meta import BaseState, StateEnum

if TYPE_CHECKING:
    from typing import TypedDict

    from pygame import Surface

    class StarConfig(TypedDict):
        size: int
        count: int
        colour: tuple[int, int, int]


class GameState(BaseState, state_name=StateEnum.GAME):
    def __init__(self) -> None:
        layers: list[Surface] = [
            pygame.Surface(
                (WINDOW_WIDTH, WINDOW_HEIGHT),
                pygame.SRCALPHA,
            )
            for _ in range(3)
        ]

        self.star_config: list[StarConfig] = [
            {
                "size": 3,
                "count": 50,
                "colour": (255, 222, 222),
            },
            {
                "size": 4,
                "count": 100,
                "colour": (172, 192, 216),
            },
            {
                "size": 5,
                "count": 150,
                "colour": (222, 255, 252),
            },
        ]
        for config, surf in zip(self.star_config, layers, strict=True):
            for _ in range(config["count"]):
                pos_x = random.randint(0, WINDOW_WIDTH)
                pos_y = random.randint(0, WINDOW_HEIGHT)
                pygame.draw.circle(
                    surf,
                    random.choice([(255, 222, 222), (172, 192, 216), (222, 255, 252)]),
                    (pos_x, pos_y),
                    config["size"],
                )

        self.space_layers = [
            SpaceLayer(
                layer,
                WINDOW_WIDTH,
                WINDOW_HEIGHT,
            )
            for layer in layers
        ]
        self.player = Player()

    def process_update(self, dt: float) -> None:
        self.window.fill((0, 0, 0))

        self.player.update(dt)

        for index, layer in enumerate(self.space_layers):
            layer.update(self.player.direction, self.player.speed * (index * 0.5), dt)
            layer.draw(self.window)
