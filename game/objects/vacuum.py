from typing import TYPE_CHECKING

from game.objects import GameObject
from lib.game.enums import GameObjectType

if TYPE_CHECKING:
    pass


class Vacuum(GameObject):
    def __init__(self):
        super().__init__()

    @property
    def type(self) -> 'GameObjectType':
        return GameObjectType.Vacuum
