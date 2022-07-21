from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from math import sqrt
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional
from typing import TYPE_CHECKING
from typing import Tuple
from uuid import UUID

from lib.game.exceptions import InvalidWorldSizeException
from lib.game.exceptions import OutOfMapException

if TYPE_CHECKING:
    from lib.game.objects import GameObject
    from lib.game.objects import GameObjectType


class Direction(Enum):
    North = 'n'
    South = 's'
    West = 'w'
    East = 'e'
    NorthWest = 'nw'
    NorthEast = 'ne'
    SouthWest = 'sw'
    SouthEast = 'se'

    @staticmethod
    def from_offset(dx: int, dy: int) -> Optional['Direction']:
        if dx > 0 and dy > 0:
            return Direction.NorthEast
        elif dx > 0 > dy:
            return Direction.SouthEast
        elif dx < 0 < dy:
            return Direction.NorthWest
        elif dx < 0 and dy < 0:
            return Direction.SouthWest
        elif dx == 0 and dy > 0:
            return Direction.North
        elif dx == 0 and dy < 0:
            return Direction.South
        elif dx > 0 and dy == 0:
            return Direction.West
        elif dx < 0 and dy == 0:
            return Direction.East
        return None

    def get_normalized_offset(self) -> Tuple[int, int]:
        dx = 0
        dy = 0

        if self == Direction.North or self == Direction.NorthEast or self == Direction.NorthWest:
            dy = 1
        elif self == Direction.South or self == Direction.SouthEast or self == Direction.SouthWest:
            dy = -1
        if self == Direction.East or self == Direction.NorthEast or self == Direction.SouthEast:
            dx = 1
        elif self == Direction.West or self == Direction.NorthWest or self == Direction.SouthWest:
            dx = -1

        return dx, dy


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __str__(self):
        return f'{self.x}, {self.y}'

    def calculate_distance(self, other_position: 'Position') -> float:
        return sqrt((self.x - other_position.x) ** 2 + (self.y - other_position.y) ** 2)

    def increment(self, dx: int, dy: int) -> 'Position':
        return Position(self.x + dx, self.y + dy)


class Map:
    def __init__(self, size_x: int, size_y: int):
        if size_x <= 0 or size_y <= 0:
            raise InvalidWorldSizeException('World size must be greater than zero')

        self.__size_x = size_x
        self.__size_y = size_y

        self.__objects: Dict[UUID, 'GameObject'] = dict()
        self.__map: Dict['Position', List] = defaultdict(list)
        self.__reversed_map: Dict[UUID, 'Position'] = dict()

    @property
    def size_x(self) -> int:
        return self.__size_x

    @property
    def size_y(self) -> int:
        return self.__size_y

    def find_object(self, object_id: UUID) -> Optional['Position']:
        return self.__reversed_map.get(object_id)

    def get_all_objects(self) -> Iterable['GameObject']:
        return list(self.__objects.values())

    def get_objects_by_type(self, object_type: 'GameObjectType') -> Iterable['GameObject']:
        return [game_object for game_object in self.get_all_objects() if game_object.type == object_type]

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

    def place_object(self, game_object: 'GameObject', position: 'Position'):
        if position.x >= self.__size_x or position.y >= self.__size_y or position.x < 0 or position.y < 0:
            raise OutOfMapException(f'Position {position} is out of map bounds')

        self.remove_object(game_object.id)

        self.__objects[game_object.id] = game_object
        self.__map[position].append(game_object.id)
        self.__reversed_map[game_object.id] = position

    def remove_object(self, object_id: UUID):
        current_object_position = self.find_object(object_id)
        if current_object_position:
            self.__objects.pop(object_id)
            self.__reversed_map.pop(object_id)
            self.__map.pop(current_object_position)
