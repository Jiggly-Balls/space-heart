from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

from space_heart.core.const import (
    DIR_GRAPHICS_NORMALS,
    DIR_GRAPHICS_RAW,
    SPACE_DRAG,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    ShaderEnum,
    ShaderRenderOrder,
)
from space_heart.core.helpers import create_vao, load_texture, screen_to_clip
from space_heart.layers.gpu import Renderable

if TYPE_CHECKING:
    from moderngl import Context, Texture
    from pygame import Vector2


class Player:
    def __init__(self, ctx: Context) -> None:
        self.ctx = ctx

        self.direction: Vector2 = pygame.Vector2()
        self.camera: Vector2 = pygame.Vector2()
        self.speed: float = 100
        self.acceleration: float = 0.1
        self.max_magnitude: float = 5.0

        self.ship_texture: Texture = load_texture(
            self.ctx, DIR_GRAPHICS_RAW / "ship09A.png"
        )
        self.ship_normals: Texture = load_texture(
            self.ctx, DIR_GRAPHICS_NORMALS / "ship09A.png"
        )

        # self.ship_vao: VertexArray = create_vao(self.ctx, ShaderEnum.SHIP_SHADOW)

        self.ship_renderable = Renderable(
            level=ShaderRenderOrder.SHIP_SHADOW,
            shader=ShaderEnum.SHIP_SHADOW,
            vao=create_vao(
                self.ctx,
                ShaderEnum.SHIP_SHADOW,
                (256, 320),
                (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 200),
            ),
            textures={
                "diffuseMap": self.ship_texture,
                "normalMap": self.ship_normals,
            },
            uniforms={
                "lightColor": (1.0, 0.95, 0.85),
                "ambientStrength": 0.25,
            },
        )

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
        if self.direction.magnitude() > self.max_magnitude:
            self.direction.scale_to_length(self.max_magnitude)

        self.camera += self.direction * self.speed * dt

    def draw(self) -> None:
        self.ship_renderable.uniforms["lightPos"] = screen_to_clip(
            *pygame.mouse.get_pos(), 1, 1
        )[0]
        self.ship_renderable.render()
