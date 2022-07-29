from typing import TYPE_CHECKING

from lib.game.enums import ComponentType

if TYPE_CHECKING:
    from client.game_client import GameClient
    from view.console.components import ComponentView


class ComponentViewFactory:
    def __init__(self, game_client: 'GameClient'):
        self.__game_client = game_client

    def create_view(self, component_type: 'ComponentType') -> 'ComponentView':
        if component_type == ComponentType.Detector:
            from view.console.components import DetectorView
            return DetectorView(game_client=self.__game_client)

        if component_type == ComponentType.SolidBody:
            from view.console.components import SolidBodyView
            return SolidBodyView(game_client=self.__game_client)
