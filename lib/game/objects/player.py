from typing import TYPE_CHECKING

from lib.game.components.detector import Detector
from lib.game.objects import GameObject
from lib.game.objects import GameObjectType

if TYPE_CHECKING:
    from lib.game import GameContext


class Player(GameObject):
    @property
    def type(self) -> 'GameObjectType':
        return GameObjectType.Player

    def __init__(self, game_context: 'GameContext'):
        super(Player, self).__init__(game_context=game_context)
        self.add_component(Detector())
