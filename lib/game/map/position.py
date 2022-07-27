from dataclasses import dataclass
from math import sqrt


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
