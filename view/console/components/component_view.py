from abc import abstractmethod
from typing import Generic
from typing import Optional
from typing import TYPE_CHECKING
from typing import TypeVar

from lib.game.state import ComponentState
from view.console.controls import Menu
from view.console.screen import Screen

if TYPE_CHECKING:
    from client.game_client import GameClient

T = TypeVar('T', bound=ComponentState)


class ComponentView(Generic[T]):
    def __init__(self, game_client: 'GameClient'):
        self._game_client = game_client

    @abstractmethod
    def render(self, state: T) -> str:
        raise NotImplementedError('Not implemented')

    def show(self, state: T):
        Screen.display(self.render(state=state))

    def get_menu(self) -> Optional[Menu]:
        return None
