from __future__ import annotations

from typing import TYPE_CHECKING

from space_heart.core.const import DIR_SHADERS_FRAG, DIR_SHADERS_VERT, ShaderEnum
from space_heart.states.meta.base_state import BaseState
from space_heart.states.meta.state_enums import StateEnum

if TYPE_CHECKING:
    from collections.abc import Callable

    type LoaderFunc = Callable[[LoaderState], None]


_funcs_to_load: list[LoaderFunc] = []


def _mark_to_load(func: LoaderFunc) -> LoaderFunc:
    _funcs_to_load.append(func)
    return func


class LoaderState(BaseState, state_name=StateEnum.LOADER_STATE):
    @_mark_to_load
    def _load_shaders(self) -> None:
        for shader in ShaderEnum:
            frag_content: str | None = None

            if shader.value.fragment:
                frag_path = DIR_SHADERS_FRAG / shader.value.fragment
                with frag_path.open("r") as f:
                    frag_content = f.read()

            vert_path = DIR_SHADERS_VERT / shader.value.vertex
            with vert_path.open("r") as f:
                vert_content = f.read()

            self.shaders[shader] = self.ctx.program(
                vertex_shader=vert_content, fragment_shader=frag_content
            )

    def on_enter(self, previous_state: BaseState | None) -> None:
        for func in _funcs_to_load:
            func(self)

        self.manager.change_state(self.manager.post_init_state)
