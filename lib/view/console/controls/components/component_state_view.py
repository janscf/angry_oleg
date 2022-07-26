from abc import abstractmethod
from typing import Generic
from typing import TypeVar

from lib.game.components import ComponentState

T = TypeVar('T', bound=ComponentState)


class ComponentStateView(Generic[T]):
    def __init__(self, component_state: 'ComponentState'):
        self.__state: T = component_state

    @property
    def state(self) -> T:
        return self.__state

    @abstractmethod
    def show_state(self):
        raise NotImplementedError('Not implemented')