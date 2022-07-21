from abc import ABC
from abc import abstractmethod
from typing import List
from typing import TYPE_CHECKING

from lib.game.exceptions.component_exceptions import MissingComponentException

if TYPE_CHECKING:
    from lib.game.components import ComponentType
    from lib.game.messages.game_message import GameMessage
    from lib.game.objects import GameObject


class ComponentState(ABC):
    @abstractmethod
    def __init__(self, component_type: 'ComponentType'):
        self.__component_type = component_type

    @property
    def component_type(self) -> 'ComponentType':
        return self.__component_type


class Component(ABC):
    dependencies: List['ComponentType'] = []

    def __init__(self, owner: 'GameObject'):
        self._owner = owner
        for component_type in self.dependencies:
            if not self._owner.has_component(component_type):
                raise MissingComponentException(f'Required component {component_type} not found in the owner object')

    @property
    @abstractmethod
    def type(self) -> 'ComponentType':
        raise NotImplementedError('Not implemented')

    @abstractmethod
    def get_state(self) -> 'ComponentState':
        raise NotImplementedError('Not implemented')

    def process_message(self, message: 'GameMessage'):
        pass
