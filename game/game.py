from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from typing import TYPE_CHECKING
from uuid import UUID
from uuid import uuid4

from game.map.builder import MapBuilder
from game.messages.update_state_message import UpdateStateMessage
from lib.game.state import GameState

if TYPE_CHECKING:
    from game.map import Map


@dataclass(frozen=True)
class MatchParameters:
    map_name: Optional[str] = None


@dataclass(frozen=True)
class PlayerDescriptor:
    player_id: UUID
    object_id: UUID
    player_name: str


class GameContext:
    def __init__(self, game: 'Game'):
        self.__game = game

    @property
    def map(self) -> 'Map':
        return self.__game.map


class Game:
    def __init__(self):
        self.__turn = 0
        self.__start_time: Optional[datetime] = None
        self.__end_time: Optional[datetime] = None
        self.__context = GameContext(self)
        self.__map = None
        self.__player: Optional[PlayerDescriptor] = None

    def add_player(self, object_id: UUID, name: str):
        self.__player = PlayerDescriptor(object_id=object_id, player_id=uuid4(), player_name=name)

    @property
    def map(self) -> Optional['Map']:
        return self.__map

    def get_state(self) -> GameState:
        all_object_states = [
            game_object.get_state() for game_object in self.__map.get_all_objects()
        ]
        player_object = self.map.get_object(self.__player.object_id)
        return GameState(
            turn=self.__turn,
            object_states=all_object_states,
            player_state=player_object.get_state(),
        )

    def is_active(self) -> bool:
        return self.__start_time is not None and self.__end_time is None

    def is_finished(self) -> bool:
        return self.__end_time is not None

    def start(self):
        self.__turn = 0
        self.__start_time = datetime.now()
        self.__end_time = None
        self.__map = MapBuilder.build_random_map()

    def end(self):
        self.__end_time = datetime.now()

    def next_turn(self):
        self.__turn += 1
        for game_object in self.__map.get_all_objects():
            game_object.send_message(UpdateStateMessage())
            game_object.update_state(self.__context)
