from dataclasses import dataclass
from typing import TYPE_CHECKING

from lib.game.enums import ComponentType
from lib.game.state import ComponentState

if TYPE_CHECKING:
    from lib.game.enums import Direction
    from lib.game.map import Position


@dataclass
class SolidBodyState(ComponentState):
    position: 'Position'
    direction: 'Direction' = None

    def __init__(self, position: 'Position', direction: 'Direction' = None):
        super(SolidBodyState, self).__init__(ComponentType.SolidBody)
        self.position = position
        self.direction = direction
