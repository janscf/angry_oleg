from game.objects import GameObject
from lib.game.enums import GameObjectType


class Exit(GameObject):
    @property
    def type(self) -> 'GameObjectType':
        return GameObjectType.Exit
