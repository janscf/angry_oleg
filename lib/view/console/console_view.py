from typing import TYPE_CHECKING

from lib.game.objects import GameObjectState
from lib.view.console.controls.screen import Screen

if TYPE_CHECKING:
    from lib.game import GameState


class ConsoleView:
    def show(self, game_state: 'GameState'):
        Screen.clear_console()

        print('-------------------------')
        print(f'Move #{game_state.turn}')
        print('-------------------------')

        player = game_state.player

        for object_state in game_state.object_states:
            if object_state.object_id != player.object_id:
                continue

            self.__show_object_state(object_state)

    def __show_object_state(self, object_state: 'GameObjectState'):
        for component_state in object_state.component_states:

        # direction_submenu = Menu(
        #     menu_items=[
        #         MenuItem(
        #             label=direction.name,
        #             shortcut=direction.value,
        #             payload=direction,
        #         ) for direction in Direction
        #     ]
        # )
        # main_menu = Menu(
        #     menu_items=[
        #         SubMenuItem(
        #             label='Move',
        #             shortcut='m',
        #             sub_menu=direction_submenu,
        #         )
        #     ]
        # )
        # print(main_menu.show_dialog())
