from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

from space_heart.core.const import SPACE_DRAG

if TYPE_CHECKING:
    from pygame import Surface, Vector2


class Player:
    def __init__(self) -> None:
        self.direction: Vector2 = pygame.Vector2()
        self.camera: Vector2 = pygame.Vector2()
        self.speed: float = 100
        self.acceleration: float = 0.1

    def update(self, dt: float) -> None:
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_w]:
            self.direction.y += -self.acceleration
        elif key_pressed[pygame.K_s]:
            self.direction.y += self.acceleration

        if key_pressed[pygame.K_d]:
            self.direction.x += self.acceleration
        elif key_pressed[pygame.K_a]:
            self.direction.x += -self.acceleration

        if self.direction.magnitude() != 0.0:
            self.direction *= SPACE_DRAG

        if self.direction.magnitude() < 0.000001:
            self.direction.update(0, 0)

        self.camera += self.direction * self.speed * dt

    def draw(self, surface: Surface) -> None: ...
