from typing import List
from typing import Optional
from uuid import UUID

from lib.game.enums import GameObjectType
from lib.game.state import ComponentState


class GameObjectState:
    def __init__(
        self,
        object_id: UUID,
        object_type: 'GameObjectType',
        component_states: List['ComponentState'],
    ):
        self.__object_id = object_id
        self.__object_type = object_type
        self.__component_states = component_states

    @property
    def object_id(self) -> Optional[UUID]:
        return self.__object_id

    @property
    def object_type(self) -> Optional['GameObjectType']:
        return self.__object_type

    @property
    def component_states(self) -> List['ComponentState']:
        return self.__component_states
