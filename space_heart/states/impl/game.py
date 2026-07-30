from __future__ import annotations

import random
from typing import TYPE_CHECKING

import pygame

from space_heart.core.background import SpaceLayer
from space_heart.core.const import WINDOW_HEIGHT, WINDOW_WIDTH
from space_heart.entities.player import Player
from space_heart.states.meta import BaseState, StateEnum

if TYPE_CHECKING:
    from pygame import Event, Surface


class GameState(BaseState, state_name=StateEnum.GAME):
    def __init__(self) -> None:
        layers: list[Surface] = [
            pygame.Surface(
                (WINDOW_WIDTH, WINDOW_HEIGHT),
                pygame.SRCALPHA,
            )
            for _ in range(3)
        ]

        for size, surf in enumerate(layers, start=1):
            for pos_x, pos_y in zip(
                random.sample(
                    range(5, WINDOW_WIDTH - 5, 2),
                    size * 50,
                ),
                random.sample(
                    range(5, WINDOW_HEIGHT - 5, 2),
                    size * 50,
                ),
                strict=True,
            ):
                pygame.draw.circle(
                    surf,
                    random.choice([(255, 222, 222), (172, 192, 216), (222, 255, 252)]),
                    (pos_x, pos_y),
                    size,
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
        self.clear: bool = True

    def process_event(self, event: Event, dt: float) -> None:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            self.clear = not self.clear
        super().process_event(event, dt)

    def process_update(self, dt: float) -> None:
        if self.clear:
            self.window.fill((0, 0, 0))

        self.player.update(dt)

        for index, layer in enumerate(self.space_layers, start=1):
            layer.update(self.player.direction, self.player.speed * (index * 0.2), dt)
            layer.draw(self.window)
