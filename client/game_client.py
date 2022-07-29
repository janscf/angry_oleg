from abc import ABC
from abc import abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lib.game.enums import Direction


class GameClient(ABC):
    @abstractmethod
    def move_to(self, direction: 'Direction'):
        raise NotImplementedError('Not implemented')

    @abstractmethod
    def go_next_turn(self):
        raise NotImplementedError('Not implemented')
