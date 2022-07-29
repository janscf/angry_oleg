from typing import TYPE_CHECKING
from typing import Tuple

from lib.game.state import GameObjectState
from view.console.controls import Menu
from view.console.controls import SubMenuItem
from view.console.screen import Screen
from .component_view_factory import ComponentViewFactory
from .controls import MenuItem

if TYPE_CHECKING:
    from lib.game.state import GameState
    from service.game_service import GameService


class _Texts:
    TURN_NUMBER_LABEL = 'Ход {turn_number}'
    NEXT_TURN_LABEL = 'Завершить ход'


class ConsoleView:
    NEXT_TURN_SHORTCUT = 'n'

    def __init__(self, game_service: 'GameService'):
        self.__service = game_service

    def show(self, game_state: 'GameState'):
        Screen.clear_console()
        Screen.display(_Texts.TURN_NUMBER_LABEL.format(turn_number=game_state.turn))

        state = game_state.player_state
        info_text, action_menu = self.__process_state(state)
        Screen.display(info_text)
        action_menu.add_menu_item(
            MenuItem(
                shortcut=self.NEXT_TURN_SHORTCUT,
                title=_Texts.NEXT_TURN_LABEL,
            )
        )
        action_menu.show_dialog()

    @staticmethod
    def __process_state(object_state: 'GameObjectState') -> Tuple[str, Menu]:
        action_menu = Menu()
        info_text = ''

        component_submenu_index = 1
        for component_state in object_state.components:
            component_view = ComponentViewFactory.create(component_state)
            if component_view:
                info_text += component_view.render()
                component_menu = component_view.get_menu()
                if component_menu:
                    action_menu.add_menu_item(
                        SubMenuItem(
                            shortcut=str(component_submenu_index),
                            title=component_menu.title,
                            sub_menu=component_menu,
                        )
                    )
                    component_submenu_index += 1

        return info_text, action_menu

    def __render_info_text(self):
        pass
