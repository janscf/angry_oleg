from game.objects import GameObject
from game.objects import GameObjectType


class Exit(GameObject):
    @property
    def type(self) -> 'GameObjectType':
        return GameObjectType.Exit
