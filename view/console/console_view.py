from typing import TYPE_CHECKING

from lib.game.state import GameObjectState
from view.console.controls import ComponentViewFactory
from view.console.controls.menu import Menu
from view.console.controls.menu import SubMenuItem
from view.console.screen import Screen

if TYPE_CHECKING:
    from lib.game.state import GameState


class ConsoleView:
    TURN_NUMBER_MESSAGE = 'Ход {turn_number}'

    def show(self, game_state: 'GameState'):
        Screen.clear_console()
        Screen.display(self.TURN_NUMBER_MESSAGE.format(turn_number=game_state.turn))

        player = game_state.player
        for object_state in game_state.object_states:
            if object_state.object_id != player.object_id:
                continue

            self.__show_object_state(object_state)
            self.__show_menu(object_state)
            input()

    def __show_object_state(self, object_state: 'GameObjectState'):
        menu = Menu()
        component_submenu_index = 1
        for component_state in object_state.component_states:
            component_view = ComponentViewFactory.create(component_state)
            if component_view:
                component_view.show_state()
                component_menu = component_view.get_actions_menu()
                if component_menu:
                    menu.add_menu_item(
                        SubMenuItem(
                            shortcut=str(component_submenu_index),
                            label=f'{component_state.component_type} menu',
                            sub_menu=component_menu,
                        )
                    )
                    component_submenu_index += 1

        print(menu.show_dialog())
