from __future__ import annotations

from space_heart.states.meta.base_state import BaseState
from space_heart.states.meta.state_enums import StateEnum


class LoaderState(BaseState, state_name=StateEnum.LOADER_STATE):
    def on_enter(self, previous_state: BaseState | None) -> None:
        self.manager.change_state(self.manager.post_init_state)
