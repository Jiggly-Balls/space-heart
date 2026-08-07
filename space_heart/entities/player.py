from __future__ import annotations

from typing import TYPE_CHECKING

import moderngl
import pygame

from space_heart.core.const import (
    DIR_GRAPHICS_NORMALS,
    DIR_GRAPHICS_RAW,
    SPACE_DRAG,
    ShaderEnum,
)
from space_heart.core.helpers import create_vao, load_texture
from space_heart.states.meta import BaseState

if TYPE_CHECKING:
    from moderngl import Context, Texture, VertexArray
    from pygame import Surface, Vector2


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
        self.ship_texture.use(0)
        self.ship_normals.use(1)

        self.ship_vao: VertexArray = create_vao(self.ctx, ShaderEnum.SHIP_SHADOW)

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

    def draw(self, surface: Surface) -> None:
        BaseState.shaders[ShaderEnum.SHIP_SHADOW]["diffuseMap"] = 0
        BaseState.shaders[ShaderEnum.SHIP_SHADOW]["normalMap"] = 1
        BaseState.shaders[ShaderEnum.SHIP_SHADOW]["lightPos"] = (
            1.0,
            1.0,
        )  # wherever your star/light source is, in uv-space
        BaseState.shaders[ShaderEnum.SHIP_SHADOW]["lightColor"] = (1.0, 0.95, 0.85)
        BaseState.shaders[ShaderEnum.SHIP_SHADOW]["ambientStrength"] = 0.25

        self.ship_vao.render(mode=moderngl.TRIANGLE_STRIP)
