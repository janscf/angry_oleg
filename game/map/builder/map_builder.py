import random
from abc import ABC

from game.map import Map
from game.objects.exit import Exit


class MapBuilder(ABC):
    @staticmethod
    def build_random_map() -> 'Map':
        size_x = random.randint(30, 100)
        size_y = random.randint(30, 100)
        game_map = Map(size_x, size_y)

        game_map.place_object_in_random_position(Exit())
        return game_map
