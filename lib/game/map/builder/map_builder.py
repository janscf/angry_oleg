from abc import ABC
from abc import abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lib.game import GameContext
    from lib.game.map.map import Map


class MapBuilder(ABC):
    @abstractmethod
    def get_map(self, game_context: 'GameContext', map_name: str = None) -> 'Map':
        raise NotImplementedError('Not Implemented')
