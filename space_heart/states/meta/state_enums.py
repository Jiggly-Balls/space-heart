from enum import StrEnum, auto

__all__ = ("StateEnum",)


class StateEnum(StrEnum):
    MAIN_MENU = auto()
    SETTINGS = auto()
    GAME = auto()
    LOADER = auto()
