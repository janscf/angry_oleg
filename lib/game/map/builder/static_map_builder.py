from typing import TYPE_CHECKING

from lib.game.map.builder import MapBuilder
from lib.game.map.map import Map
from lib.game.map.map import Position
from lib.game.objects.vacuum import Vacuum

if TYPE_CHECKING:
    from lib.game import GameContext


class StaticMapBuilder(MapBuilder):
    def get_map(self, game_context: 'GameContext', map_name: str = None) -> 'Map':
        game_map = Map(100, 100)
        vacuum = Vacuum(game_context)
        game_map.place_object(vacuum, Position(2, 2))
        return game_map
