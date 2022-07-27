from dataclasses import dataclass
from typing import Iterable
from typing import TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from lib.game.enums import GameObjectType
    from lib.game.state import ComponentState


@dataclass(frozen=True)
class GameObjectState:
    object_id: UUID
    object_type: 'GameObjectType'
    component_states: Iterable['ComponentState']
