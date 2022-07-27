from abc import abstractmethod
from typing import Generic
from typing import Iterable
from typing import TYPE_CHECKING
from typing import TypeVar

from game.exceptions.component_exceptions import MissingComponentException
from lib.game.state import ComponentState

if TYPE_CHECKING:
    from game import GameContext
    from lib.game.enums import ComponentType
    from game.messages.game_message import GameMessage
    from game.objects import GameObject


T = TypeVar('T', bound=ComponentState)


class Component(Generic[T]):
    dependencies: Iterable['ComponentType'] = []

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
    def get_state(self, context: 'GameContext') -> T:
        raise NotImplementedError('Not implemented')

    def process_message(self, message: 'GameMessage', context: 'GameContext'):
        pass
