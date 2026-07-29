from space_heart.states.meta import BaseState, StateEnum


class GameState(BaseState, state_name=StateEnum.GAME):
    def process_update(self, dt: float) -> None:
        self.window.fill((0, 0, 0))
