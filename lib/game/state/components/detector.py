from dataclasses import dataclass
from typing import Iterable
from typing import TYPE_CHECKING

from lib.game.enums import ComponentType
from lib.game.state import ComponentState

if TYPE_CHECKING:
    from lib.game.enums import Direction
    from lib.game.enums import SignalLevel


@dataclass(frozen=True)
class TargetSignal:
    direction: 'Direction'
    signal_level: 'SignalLevel'


@dataclass
class DetectorState(ComponentState):
    targets: Iterable[TargetSignal]

    def __init__(self, targets: Iterable[TargetSignal]):
        super(DetectorState, self).__init__(ComponentType.Detector)
        self.targets = targets
