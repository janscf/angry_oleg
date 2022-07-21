from abc import ABC
from abc import abstractmethod
from collections import deque
from typing import List
from typing import Optional
from typing import TYPE_CHECKING
from uuid import UUID
from uuid import uuid4

from lib.game.exceptions import DuplicateComponentException

if TYPE_CHECKING:
    from lib.game import GameContext
    from lib.game.components import Component
    from lib.game.components import ComponentState
    from lib.game.components import ComponentType
    from lib.game.messages import GameMessage
    from lib.game.objects import GameObjectType


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


class GameObject(ABC):
    def __init__(self, game_context: 'GameContext'):
        self.__id = uuid4()
        self._components: List['Component'] = []
        self._game_context = game_context
        self._messages = deque()

    @property
    @abstractmethod
    def type(self) -> 'GameObjectType':
        raise NotImplementedError('Not implemented')

    @property
    def id(self) -> UUID:
        return self.__id

    @property
    def game_context(self) -> 'GameContext':
        return self._game_context

    def get_state(self) -> GameObjectState:
        return GameObjectState(
            object_id=self.id,
            object_type=self.type,
            component_states=[component.get_state(self._game_context) for component in self._components],
        )

    def has_component(self, component_type: 'ComponentType') -> bool:
        return any(c.type == component_type for c in self._components)

    def add_component(self, component: 'Component'):
        if self.has_component(component.type):
            raise DuplicateComponentException(f'Component {component.type} is already added')
        self._components.append(component)

    def send_message(self, message: 'GameMessage'):
        self._messages.append(message)

    def update_state(self):
        while self._messages:
            message = self._messages.popleft()
            for component in self._components:
                component.process_message(message, self._game_context)
