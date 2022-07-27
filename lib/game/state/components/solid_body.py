from lib.game.enums import ComponentType
from lib.game.enums import Direction
from lib.game.map import Position
from lib.game.state import ComponentState


class SolidBodyState(ComponentState):
    def __init__(self, position: 'Position', direction: 'Direction' = None):
        super(SolidBodyState, self).__init__(ComponentType.SolidBody)
        self.__position = position
        self.__direction = direction

    @property
    def position(self) -> 'Position':
        return self.__position

    @property
    def direction(self) -> 'Direction':
        return self.__direction
