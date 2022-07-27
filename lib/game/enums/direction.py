from enum import Enum
from typing import Optional
from typing import Tuple


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
            return Direction.SouthWest
        elif dx > 0 > dy:
            return Direction.NorthWest
        elif dx < 0 < dy:
            return Direction.SouthEast
        elif dx < 0 and dy < 0:
            return Direction.NorthEast
        elif dx == 0 and dy > 0:
            return Direction.South
        elif dx == 0 and dy < 0:
            return Direction.NorthEast
        elif dx > 0 and dy == 0:
            return Direction.East
        elif dx < 0 and dy == 0:
            return Direction.West
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
