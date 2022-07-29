from typing import Any
from typing import Iterable
from typing import List
from typing import Optional
from typing import TYPE_CHECKING

from ..screen import Screen

if TYPE_CHECKING:
    from ...commands import Command


class MenuItem:
    def __init__(self, title: str, shortcut: str, payload: Any = None, command: 'Command' = None):
        self.label = title
        self.shortcut = shortcut
        self.payload = payload
        self.command = command

    def on_select(self):
        if self.command:
            self.command.execute(self.payload)


class Menu:
    def __init__(self, title: str = '', menu_items: List[MenuItem] = None, default_input: str = None):
        self.__title = title
        self.__menu_items = menu_items or []
        self.selected_item = None
        self.default_input = default_input

    @property
    def title(self) -> str:
        return self.__title

    @property
    def menu_items(self) -> Iterable[MenuItem]:
        return self.__menu_items

    def add_menu_item(self, menu_item: MenuItem):
        self.__menu_items.append(menu_item)

    def show_dialog(self) -> Any:
        for item in self.__menu_items:
            Screen.display(f'{item.shortcut}. {item.label}')

        self.selected_item = self.__wait_for_user_input()
        return self.selected_item.payload

    def __wait_for_user_input(self) -> MenuItem:
        selected_item = None
        while selected_item is None:
            shortcut = input().strip() or self.default_input
            selected_item = self.__get_selected_item(shortcut=shortcut)

        return selected_item

    def __get_selected_item(self, shortcut: str) -> Optional[MenuItem]:
        for item in self.__menu_items:
            if item.shortcut == shortcut:
                item.on_select()
                return item


class SubMenuItem(MenuItem):
    def __init__(self, title: str, shortcut: str, sub_menu: Menu, command: 'Command' = None):
        super(SubMenuItem, self).__init__(title=title, shortcut=shortcut, command=command)
        self.sub_menu = sub_menu

    def on_select(self):
        self.payload = self.sub_menu.show_dialog()
        super(SubMenuItem, self).on_select()
