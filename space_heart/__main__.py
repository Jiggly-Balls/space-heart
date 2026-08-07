from __future__ import annotations

import array
from typing import TYPE_CHECKING

import moderngl
import pygame

from space_heart.core.const import (
    FPS,
    GAME_TITLE,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    ShaderEnum,
)
from space_heart.core.helpers import surface_to_texture
from space_heart.states.impl import GameState
from space_heart.states.meta import BaseManager, BaseState, LoaderState, StateEnum


def main() -> None:
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)
    pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF
    )
    clock = pygame.time.Clock()
    ctx = moderngl.create_context()
    window = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), flags=pygame.SRCALPHA)

    state_manager = BaseManager(
        post_init_state=StateEnum.GAME,
        bound_state_type=BaseState,
        window=window,
        ctx=ctx,
    )
    state_manager.load_states(LoaderState, GameState)
    state_manager.change_state(StateEnum.LOADER_STATE)
    if TYPE_CHECKING:
        assert state_manager.current_state is not None

    # fmt: off
    quad_data = ctx.buffer(
        array.array(
            "f",
            [
                -1.0, -1.0, 0.0, 1.0,
                 1.0, -1.0, 1.0, 1.0,
                -1.0,  1.0, 0.0, 0.0,
                 1.0,  1.0, 1.0, 0.0,
            ],
        )
    )
    # fmt: on
    quad_vao = ctx.vertex_array(
        BaseState.shaders[ShaderEnum.QUAD],
        [(quad_data, "2f 2f", "in_position", "in_uv")],
    )

    while state_manager.is_running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            state_manager.current_state.process_event(event, dt)
        state_manager.current_state.process_update(dt)

        frame_tex = surface_to_texture(ctx, window)
        frame_tex.use(0)
        BaseState.shaders[ShaderEnum.QUAD]["tex"] = 0
        quad_vao.render(mode=moderngl.TRIANGLE_STRIP)

        pygame.display.flip()

        frame_tex.release()


if __name__ == "__main__":
    main()
    pygame.quit()
