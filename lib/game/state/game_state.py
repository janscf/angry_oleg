from typing import List

from lib.game.state import GameObjectState


class GameState:
    def __init__(self, turn: int, object_states: List['GameObjectState'], player: GameObjectState):
        self.__turn = turn
        self.__object_states = object_states
        self.__player = player

    @property
    def turn(self) -> int:
        return self.__turn

    @property
    def object_states(self) -> List['GameObjectState']:
        return self.__object_states

    @property
    def player(self) -> GameObjectState:
        return self.__player
