from __future__ import annotations

from typing import TYPE_CHECKING

import pygame
from game_state import State
from game_state.utils import MISSING

if TYPE_CHECKING:
    from moderngl import Context, Program
    from pygame import Event, Surface

    from space_heart.core.const import ShaderEnum
    from space_heart.states.meta.base_manager import BaseManager


__all__ = ("BaseState",)


class BaseState(State["BaseState"]):
    manager: BaseManager
    window: Surface = MISSING
    ctx: Context = MISSING
    shaders: dict[ShaderEnum, Program] = {}

    def process_update(self, dt: float) -> None: ...

    def process_event(self, event: Event, dt: float) -> None:
        if event.type == pygame.QUIT:
            self.handle_quit()

    def handle_quit(self) -> None:
        self.manager.is_running = False

        # Additional stuff to do before fully quitting
