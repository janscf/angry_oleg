from abc import abstractmethod
from typing import Generic
from typing import Optional
from typing import TypeVar

from lib.game.state import ComponentState
from view.console.controls import Menu
from view.console.screen import Screen

T = TypeVar('T', bound=ComponentState)


class ComponentView(Generic[T]):
    def __init__(self, component_state: 'ComponentState'):
        self.__state: T = component_state

    @property
    def state(self) -> T:
        return self.__state

    @abstractmethod
    def render(self) -> str:
        raise NotImplementedError('Not implemented')

    def show(self):
        Screen.display(self.render())

    def get_menu(self) -> Optional[Menu]:
        return None
