from __future__ import annotations

from typing import TYPE_CHECKING

import moderngl
import pygame

if TYPE_CHECKING:
    from pathlib import Path

    from moderngl import Context, Texture


__all__ = ("load_texture",)

def load_texture(ctx: Context, path: Path) -> Texture:
    img = pygame.image.load(str(path)).convert_alpha()

    texture = ctx.texture(img.get_size(), 4)
    texture.filter = (moderngl.NEAREST, moderngl.NEAREST)
    texture.swizzle = "BGRA"
    texture.write(img.get_view("1"))

    return texture
