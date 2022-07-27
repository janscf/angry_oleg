from typing import Optional

from lib.game.enums import Direction
from lib.game.state.components import SolidBodyState
from view.console.controls.components import ComponentStateView
from view.console.controls.direction_label import DirectionLabel
from view.console.controls.menu import Menu
from view.console.controls.menu import MenuItem
from view.console.screen import Screen


class SolidBodyView(ComponentStateView[SolidBodyState]):
    POSITION_MESSAGE = 'Ваши координаты: {coordinates}.'
    DIRECTION_MESSAGE = 'Вы двигаетесь на {direction}.'
    DIRECTION_NOT_SET_MESSAGE = 'Вы стоите на месте.'
    CHANGE_DIRECTION_LABEL = 'Двигаться на {direction}'
    STAY_LABEL = 'Оставаться на месте'

    def show_state(self):
        Screen.display(self.POSITION_MESSAGE.format(coordinates=str(self.state.position)))
        if self.state.direction:
            direction_label = DirectionLabel(self.state.direction)
            Screen.display(self.DIRECTION_MESSAGE.format(direction=direction_label))
        else:
            Screen.display(self.DIRECTION_NOT_SET_MESSAGE)

    def get_actions_menu(self) -> Optional[Menu]:
        menu_items = []

        for index, direction in enumerate(Direction):
            shortcut = str(index + 1)
            direction_label = DirectionLabel(direction)
            menu_items.append(
                MenuItem(shortcut=shortcut, label=self.CHANGE_DIRECTION_LABEL.format(direction=direction_label))
            )

        menu_items.append(
            MenuItem(shortcut='0', label=self.STAY_LABEL)
        )
        return Menu(menu_items=menu_items)
