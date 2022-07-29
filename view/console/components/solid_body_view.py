from typing import Optional

from client.commands import MoveCommand
from lib.game.enums import Direction
from lib.game.state.components import SolidBodyState
from view.console.components import ComponentView
from view.console.controls import DirectionLabel
from view.console.controls import Menu
from view.console.controls import MenuItem
from view.console.screen import Screen


class _Texts:
    POSITION_MESSAGE = 'Ваши координаты: {coordinates}.'
    DIRECTION_MESSAGE = 'Вы двигаетесь на {direction}.'
    DIRECTION_NOT_SET_MESSAGE = 'Вы стоите на месте.'

    MOVE_MENU_CHANGE_DIRECTION_LABEL = 'Двигаться на {direction}'
    MOVE_MENU_STAY_OPTION = 'Оставаться на месте'
    MOVE_MENU_TITLE = 'Движение'


class SolidBodyView(ComponentView[SolidBodyState]):
    def render(self, state: SolidBodyState):
        messages = [_Texts.POSITION_MESSAGE.format(coordinates=str(state.position))]
        if state.direction:
            direction_label = DirectionLabel(state.direction)
            messages.append(_Texts.DIRECTION_MESSAGE.format(direction=direction_label))
        else:
            messages.append(_Texts.DIRECTION_NOT_SET_MESSAGE)

        return Screen.join(messages)

    def get_menu(self) -> Optional[Menu]:
        menu_items = []

        for index, direction in enumerate(Direction):
            shortcut = str(index + 1)
            direction_label = DirectionLabel(direction)
            menu_items.append(
                MenuItem(
                    shortcut=shortcut,
                    title=_Texts.MOVE_MENU_CHANGE_DIRECTION_LABEL.format(
                        direction=direction_label,
                    ),
                    command=MoveCommand(self._game_client),
                    payload=direction,
                )
            )

        menu_items.append(MenuItem(shortcut='0', title=_Texts.MOVE_MENU_STAY_OPTION))
        return Menu(title=_Texts.MOVE_MENU_TITLE, menu_items=menu_items)
