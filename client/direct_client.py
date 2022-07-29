from typing import TYPE_CHECKING
from uuid import UUID

from client.game_client import GameClient
from game.messages import ChangeDirectionMessage

if TYPE_CHECKING:
    from game import Game
    from lib.game.enums import Direction


class DirectClient(GameClient):
    def __init__(self, player_id: UUID, game: 'Game'):
        self.__player_id = player_id
        self.__game = game

    def move_to(self, direction: 'Direction'):
        player = self.__game.get_player(self.__player_id)
        game_object = self.__game.map.get_object(player.object_id)
        game_object.send_message(ChangeDirectionMessage(direction))

    def go_next_turn(self):
        self.__game.next_turn()
