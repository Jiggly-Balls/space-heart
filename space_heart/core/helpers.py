from __future__ import annotations

import array
from typing import TYPE_CHECKING

import moderngl
import pygame

from space_heart.states.meta import BaseState

if TYPE_CHECKING:
    from pathlib import Path

    from moderngl import Context, Texture, VertexArray

    from space_heart.core.const import ShaderEnum

__all__ = (
    "create_vao",
    "load_texture",
)


def load_texture(ctx: Context, path: Path) -> Texture:
    img = pygame.image.load(str(path)).convert_alpha()

    texture = ctx.texture(img.get_size(), 4)
    texture.filter = (moderngl.NEAREST, moderngl.NEAREST)
    texture.swizzle = "BGRA"
    texture.write(img.get_view("1"))

    return texture


def create_vao(ctx: Context, shader: ShaderEnum) -> VertexArray:
    # fmt: off
    quad_data = ctx.buffer(
        array.array(
            "f",
            [
                # x ,   y ,  u ,  v
                -1.0, -1.0, 0.0, 1.0,
                 1.0, -1.0, 1.0, 1.0,
                -1.0,  1.0, 0.0, 0.0,
                 1.0,  1.0, 1.0, 0.0,
            ],
        )
    )
    # fmt: on
    quad_vao = ctx.vertex_array(
        BaseState.shaders[shader],
        [(quad_data, "2f 2f", "in_position", "in_uv")],
    )
    return quad_vao
