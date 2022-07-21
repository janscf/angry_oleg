from uuid import UUID

from lib.game.messages.game_message import GameMessage


class CollisionMessage(GameMessage):
    def __init__(self, collided_object_id: UUID):
        super(CollisionMessage, self).__init__()
        self.__collided_object_id = collided_object_id

    @property
    def collided_object_id(self) -> UUID:
        return self.__collided_object_id
