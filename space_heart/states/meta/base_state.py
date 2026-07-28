from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING

import pygame
from game_state import State

if TYPE_CHECKING:
    from pygame import Event, Surface

    from space_heart.states.meta.base_manager import BaseManager


__all__ = ("BaseState",)


class BaseState(State["BaseState"], ABC):
    manager: BaseManager  # pyright: ignore[reportIncompatibleVariableOverride]
    window: Surface

    def process_update(self, dt: float) -> None: ...

    def process_event(self, event: Event, dt: float) -> None:
        if event.type == pygame.QUIT:
            self.handle_quit()

    def handle_quit(self) -> None:
        self.manager.is_running = False

        # Additional stuff to do before fully quitting
