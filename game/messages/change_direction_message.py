from typing import TYPE_CHECKING

from game.messages.game_message import GameMessage

if TYPE_CHECKING:
    from lib.game.enums import Direction


class ChangeDirectionMessage(GameMessage):
    def __init__(self, new_direction: 'Direction'):
        super(ChangeDirectionMessage, self).__init__()
        self.__new_direction = new_direction

    @property
    def new_direction(self) -> 'Direction':
        return self.__new_direction
