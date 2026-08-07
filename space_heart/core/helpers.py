from __future__ import annotations

from typing import TYPE_CHECKING

import moderngl

if TYPE_CHECKING:
    from moderngl import Context, Texture
    from pygame import Surface


__all__ = ("surface_to_texture",)


def surface_to_texture(ctx: Context, surf: Surface) -> Texture:
    texture = ctx.texture(surf.get_size(), 4)
    texture.filter = (moderngl.NEAREST, moderngl.NEAREST)
    texture.swizzle = "BGRA"
    texture.write(surf.get_view("1"))
    return texture
