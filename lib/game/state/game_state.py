from dataclasses import dataclass
from typing import Iterable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lib.game.state import GameObjectState


@dataclass(frozen=True)
class GameState:
    turn: int
    object_states: Iterable['GameObjectState']
    player_state: 'GameObjectState'
