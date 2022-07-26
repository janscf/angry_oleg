from typing import TYPE_CHECKING
from typing import Tuple

from client.commands import NextTurnCommand
from client.game_client import GameClient
from lib.game.state import GameObjectState
from view.console.controls import Menu
from view.console.controls import SubMenuItem
from view.console.screen import Screen
from .component_view_factory import ComponentViewFactory
from .controls import MenuItem

if TYPE_CHECKING:
    from lib.game.state import GameState


class _Texts:
    TURN_NUMBER_LABEL = 'Ход {turn_number}'
    NEXT_TURN_LABEL = 'Завершить ход'


class ConsoleView:
    NEXT_TURN_SHORTCUT = 'n'

    def __init__(self, game_client: 'GameClient'):
        self.__game_client = game_client

    def show(self, game_state: 'GameState'):
        state = game_state.player_state
        info_text, action_menu = self.__process_state(state)
        next_turn_menu_item = MenuItem(
            shortcut=self.NEXT_TURN_SHORTCUT,
            title=_Texts.NEXT_TURN_LABEL,
            command=NextTurnCommand(self.__game_client),
        )
        action_menu.add_menu_item(next_turn_menu_item)
        action_menu.default_input = next_turn_menu_item.shortcut

        Screen.clear_console()
        Screen.display(_Texts.TURN_NUMBER_LABEL.format(turn_number=game_state.turn))
        Screen.display(info_text)
        action_menu.show_dialog()

    def __process_state(self, object_state: 'GameObjectState') -> Tuple[str, Menu]:
        action_menu = Menu()
        messages = []

        component_submenu_index = 1
        for component_state in object_state.components:
            component_factory = ComponentViewFactory(game_client=self.__game_client)
            component_view = component_factory.create_view(component_state.component_type)

            if component_view:
                messages.append(component_view.render(component_state))
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

        return Screen.join(messages), action_menu

    def __render_info_text(self):
        pass
