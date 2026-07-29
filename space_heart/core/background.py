from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from pygame import Surface, Vector2


class SpaceLayer:
    def __init__(self, surface: Surface, width: int, height: int) -> None:
        self.image: Surface = surface
        self.width: int = width
        self.height: int = height
        self.offset_pos: Vector2 = pygame.Vector2()

    def update(self, direction: Vector2, speed: float, dt: float) -> None:
        self.offset_pos -= speed * direction * dt
        self.offset_pos.x %= self.width
        self.offset_pos.y %= self.height

    def draw(self, surface: Surface) -> None:
        x = int(self.offset_pos.x)
        y = int(self.offset_pos.y)
        surface.blit(self.image, (x - self.width, y - self.height))
        surface.blit(self.image, (x, y - self.height))
        surface.blit(self.image, (x - self.width, y))
        surface.blit(self.image, (x, y))
