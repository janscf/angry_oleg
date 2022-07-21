from dataclasses import dataclass
from datetime import datetime
from typing import List
from typing import Optional
from typing import TYPE_CHECKING
from uuid import UUID
from uuid import uuid4

from lib.game.messages.update_state_message import UpdateStateMessage

if TYPE_CHECKING:
    from lib.game.map import Map
    from lib.game.map.builder import MapBuilder
    from lib.game.objects import GameObjectState


@dataclass(frozen=True)
class MatchParameters:
    map_name: Optional[str] = None


@dataclass(frozen=True)
class PlayerDescriptor:
    player_id: UUID
    object_id: UUID
    name: str


class GameContext:
    def __init__(self, game: 'Game'):
        self.__game = game

    @property
    def map(self) -> 'Map':
        return self.__game.map


class GameState:
    def __init__(self, turn: int, object_states: List['GameObjectState'], player: PlayerDescriptor):
        self.__turn = turn
        self.__object_states = object_states
        self.__player = player

    @property
    def turn(self) -> int:
        return self.__turn

    @property
    def object_states(self) -> List['GameObjectState']:
        return self.__object_states

    @property
    def player(self) -> PlayerDescriptor:
        return self.__player


class Game:
    def __init__(self, map_loader: 'MapBuilder'):
        self.__turn = 0
        self.__start_time: Optional[datetime] = None
        self.__end_time: Optional[datetime] = None
        self.__context = GameContext(self)
        self.__map_loader = map_loader
        self.__map = None
        self.__player = None

    def add_player(self, object_id: UUID, name: str):
        self.__player = PlayerDescriptor(object_id=object_id, player_id=uuid4(), name=name)

    @property
    def map(self) -> Optional['Map']:
        return self.__map

    def get_state(self) -> GameState:
        all_object_states = [game_object.get_state() for game_object in self.__map.get_all_objects()]
        return GameState(
            turn=self.__turn,
            object_states=all_object_states,
            player=self.__player,
        )

    def is_active(self) -> bool:
        return self.__start_time is not None and self.__end_time is None

    def is_finished(self) -> bool:
        return self.__end_time is not None

    def start(self, parameters: MatchParameters):
        self.__turn = 0
        self.__start_time = datetime.now()
        self.__end_time = None
        self.__map = self.__map_loader.get_map(self.__context, parameters.map_name)

    def end(self):
        self.__end_time = datetime.now()

    def next_turn(self):
        self.__turn += 1
        for game_object in self.__map.get_all_objects():
            game_object.send_message(UpdateStateMessage())
            game_object.update_state()
