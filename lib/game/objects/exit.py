from lib.game.objects import GameObject
from lib.game.objects import GameObjectType


class Exit(GameObject):
    @property
    def type(self) -> 'GameObjectType':
        return GameObjectType.Exit
