from typing import Optional
from typing import TYPE_CHECKING

from lib.game.objects import GameObject
from lib.game.objects import GameObjectType

if TYPE_CHECKING:
    from lib.game import GameContext


class Vacuum(GameObject):
    def __init__(self, game_context: Optional['GameContext'] = None):
        super().__init__(game_context)

    @property
    def type(self) -> 'GameObjectType':
        return GameObjectType.Vacuum
