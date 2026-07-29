from __future__ import annotations

from typing import TYPE_CHECKING

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
    def _generate_space_sheets(self) -> None:
        ...

    def on_enter(self, previous_state: BaseState | None) -> None:
        for func in _funcs_to_load:
            func(self)

        self.manager.change_state(self.manager.post_init_state)
