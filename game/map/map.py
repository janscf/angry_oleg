import random
from collections import defaultdict
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional
from typing import TYPE_CHECKING
from uuid import UUID

from game.exceptions import InvalidWorldSizeException
from game.exceptions import OutOfMapException
from lib.game.enums import Direction
from lib.game.map import Position

if TYPE_CHECKING:
    from game.objects import GameObject
    from lib.game.enums import GameObjectType


class Map:
    def __init__(self, size_x: int, size_y: int):
        if size_x <= 0 or size_y <= 0:
            raise InvalidWorldSizeException('World size must be greater than zero')

        self.__size_x = size_x
        self.__size_y = size_y

        self.__objects: Dict[UUID, 'GameObject'] = dict()
        self.__map: Dict['Position', List] = defaultdict(list)
        self.__reversed_map: Dict[UUID, 'Position'] = dict()
        self.__object_types: Dict['GameObjectType', List] = defaultdict(list)

    @property
    def size_x(self) -> int:
        return self.__size_x

    @property
    def size_y(self) -> int:
        return self.__size_y

    def get_object(self, object_id: UUID) -> Optional['GameObject']:
        return self.__objects.get(object_id)

    def find_object(self, object_id: UUID) -> Optional['Position']:
        return self.__reversed_map.get(object_id)

    def get_all_objects(self) -> Iterable['GameObject']:
        return list(self.__objects.values())

    def get_objects_by_type(self, object_type: 'GameObjectType') -> Iterable['GameObject']:
        object_ids = self.__object_types.get(object_type, [])
        return [self.__objects[object_id] for object_id in object_ids]

    def get_objects_in_position(self, position: 'Position') -> Iterable['GameObject']:
        object_ids = self.__map.get(position, [])
        return [self.__objects[object_id] for object_id in object_ids]

    def get_distance(self, object_from_id: UUID, object_to_id: UUID) -> float:
        position_from = self.find_object(object_from_id)
        position_to = self.find_object(object_to_id)
        return position_from.calculate_distance(position_to)

    def get_direction(self, object_from_id: UUID, object_to_id: UUID) -> Direction:
        position_from = self.find_object(object_from_id)
        position_to = self.find_object(object_to_id)
        delta_x = position_from.x - position_to.x
        delta_y = position_from.y - position_to.y
        return Direction.from_offset(delta_x, delta_y)

    def is_valid_position(self, position: 'Position') -> bool:
        return self.__size_x > position.x > 0 and self.__size_y > position.y > 0

    def place_object(self, game_object: 'GameObject', position: 'Position'):
        if not self.is_valid_position(position):
            raise OutOfMapException(f'Position {position} is out of map bounds')

        self.remove_object(game_object.id)

        self.__objects[game_object.id] = game_object
        self.__map[position].append(game_object.id)
        self.__reversed_map[game_object.id] = position
        self.__object_types[game_object.type].append(game_object.id)

    def place_object_in_random_position(self, game_object: 'GameObject'):
        position = Position(
            x=random.randint(1, self.size_x - 1),
            y=random.randint(1, self.size_y - 1),
        )
        self.place_object(game_object, position)

    def remove_object(self, object_id: UUID):
        current_object_position = self.find_object(object_id)
        if current_object_position:
            game_object = self.__objects[object_id]
            self.__objects.pop(object_id)
            self.__reversed_map.pop(object_id)
            self.__map[current_object_position].remove(object_id)
            self.__object_types[game_object.type].remove(object_id)
