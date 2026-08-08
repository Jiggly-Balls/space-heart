from __future__ import annotations

import array
from typing import TYPE_CHECKING

import moderngl
import pygame

from space_heart.core.const import WINDOW_HEIGHT, WINDOW_WIDTH
from space_heart.states.meta import BaseState

if TYPE_CHECKING:
    from pathlib import Path

    from moderngl import Context, Texture, VertexArray

    from space_heart.core.const import ShaderEnum

    type Clip = tuple[
        tuple[float, float],
        tuple[float, float],
        tuple[float, float],
        tuple[float, float],
    ]

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


def screen_to_clip(x: int, y: int, width: int, height: int) -> Clip:
    left = (x / WINDOW_WIDTH) * 2.0 - 1.0
    right = ((x + width) / WINDOW_WIDTH) * 2.0 - 1.0
    top = 1.0 - (y / WINDOW_HEIGHT) * 2.0
    bottom = 1.0 - ((y + height) / WINDOW_HEIGHT) * 2.0

    return (
        (left, bottom),
        (right, bottom),
        (left, top),
        (right, top),
    )


def create_vao(
    ctx: Context,
    shader: ShaderEnum,
    size: tuple[int, int],
    position: tuple[int, int],
) -> VertexArray:

    left_bottom, right_bottom, left_top, right_top = screen_to_clip(
        *position,
        *size,
    )
    # fmt: off
    quad_data = ctx.buffer(
        array.array(
            "f",
            [
                # x, y       , u  ,  v
                *left_bottom , 0.0, 1.0,
                *right_bottom, 1.0, 1.0,
                *left_top    , 0.0, 0.0,
                *right_top   , 1.0, 0.0,
            ],
        )
    )
    # fmt: on
    quad_vao = ctx.vertex_array(
        BaseState.shaders[shader],
        [(quad_data, "2f 2f", "in_position", "in_uv")],
    )
    return quad_vao
