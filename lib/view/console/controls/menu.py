from typing import Any
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

from ..screen import Screen

if TYPE_CHECKING:
    from ...commands import Command


class MenuItem:
    def __init__(self, label: str, shortcut: str, payload: Any = None):
        self.label = label
        self.shortcut = shortcut
        self.payload = payload


class Menu:
    def __init__(self, menu_items: List[MenuItem], command: 'Command' = None):
        self.__menu_items = menu_items
        self.selected_item = None
        self.command = command

    def show_dialog(self):
        for item in self.__menu_items:
            Screen.display(f'{item.shortcut}. {item.label}')

        self.selected_item = self.wait_for_user_input()
        if isinstance(self.selected_item, SubMenuItem):
            return self.selected_item.sub_menu.show_dialog()

        return self.selected_item.payload

    def wait_for_user_input(self) -> MenuItem:
        selected_item = None
        while selected_item is None:
            shortcut = input().strip()
            selected_item = self.__get_selected_item(shortcut=shortcut)

        return selected_item

    def __get_selected_item(self, shortcut: str) -> Optional[MenuItem]:
        for item in self.__menu_items:
            if item.shortcut == shortcut:
                return item


class SubMenuItem(MenuItem):
    def __init__(self, label: str, shortcut: str, sub_menu: Menu, payload: Any = 'None'):
        super(SubMenuItem, self).__init__(label, shortcut, payload)
        self.sub_menu = sub_menu
