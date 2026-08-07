from __future__ import annotations

from typing import TYPE_CHECKING

import moderngl

from space_heart.states.meta import BaseState

if TYPE_CHECKING:
    from moderngl import Program, Texture, VertexArray

    from space_heart.core.const import ShaderEnum, ShaderRenderOrder


__all__ = ("Renderable",)


class Renderable:
    instances: dict[ShaderRenderOrder, Renderable] = {}

    def __init__(
        self,
        *,
        level: ShaderRenderOrder,
        shader: ShaderEnum,
        vao: VertexArray,
        textures: dict[str, Texture] | None = None,
        uniforms: dict[str, object] | None = None,
        render_mode: int = moderngl.TRIANGLE_STRIP,
    ) -> None:
        self.instances[level] = self

        self.shader: ShaderEnum = shader
        self.vao: VertexArray = vao
        self.textures: dict[str, Texture] = textures or {}
        self.uniforms: dict[str, object] = uniforms or {}
        self.render_mode: int = render_mode

    @property
    def program(self) -> Program:
        return BaseState.shaders[self.shader]

    def render(self) -> None:
        for unit, (uniform_name, texture) in enumerate(self.textures.items()):
            texture.use(unit)
            self.program[uniform_name] = unit

        for name, value in self.uniforms.items():
            self.program[name] = value

        self.vao.render(mode=self.render_mode)
