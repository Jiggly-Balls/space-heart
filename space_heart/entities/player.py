from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from pygame import Surface, Vector2


class Player:
    def __init__(self) -> None:
        self.direction: Vector2 = pygame.Vector2()
        self.camera: Vector2 = pygame.Vector2()
        self.speed: float = 200.0

    def update(self, dt: float) -> None:
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_w]:
            self.direction.y = -1
        elif key_pressed[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if key_pressed[pygame.K_d]:
            self.direction.x = 1
        elif key_pressed[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if self.direction.magnitude() != 0.0:
            self.direction.normalize_ip()

        self.camera += self.direction * self.speed * dt

    def draw(self, surface: Surface) -> None: ...
