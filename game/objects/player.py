from typing import TYPE_CHECKING

from game.components.detector import Detector
from game.components.solid_body import SolidBody
from game.map import Direction
from game.objects import GameObject
from game.objects import GameObjectType

if TYPE_CHECKING:
    pass


class Player(GameObject):
    @property
    def type(self) -> 'GameObjectType':
        return GameObjectType.Player

    def __init__(self):
        super(Player, self).__init__()
        self.add_component(Detector(owner=self, target_type=GameObjectType.Exit))
        self.add_component(SolidBody(owner=self, direction=Direction.East))
