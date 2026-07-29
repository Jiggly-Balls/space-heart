from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

from space_heart.core.const import GAME_TITLE, WINDOW_HEIGHT, WINDOW_WIDTH
from space_heart.states.impl import GameState
from space_heart.states.meta import BaseManager, BaseState, LoaderState, StateEnum


def main() -> None:
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    state_manager = BaseManager(
        post_init_state=StateEnum.GAME,
        bound_state_type=BaseState,
        window=window,
    )
    state_manager.load_states(LoaderState, GameState)
    state_manager.change_state(StateEnum.LOADER_STATE)
    if TYPE_CHECKING:
        assert state_manager.current_state is not None

    while state_manager.is_running:
        dt = clock.tick(60.0) / 1000

        for event in pygame.event.get():
            state_manager.current_state.process_event(event, dt)
        state_manager.current_state.process_update(dt)

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
