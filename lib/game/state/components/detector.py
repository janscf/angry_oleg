from dataclasses import dataclass
from enum import Enum
from enum import auto
from typing import Iterable

from lib.game.enums import ComponentType
from lib.game.enums import Direction
from lib.game.state import ComponentState


class SignalLevel(Enum):
    High = auto()
    Average = auto()
    Low = auto()


@dataclass(frozen=True)
class TargetSignal:
    direction: 'Direction'
    signal_level: 'SignalLevel'


class DetectorState(ComponentState):
    def __init__(self, targets: Iterable[TargetSignal]):
        super(DetectorState, self).__init__(ComponentType.Detector)
        self.__targets = targets

    @property
    def targets(self):
        return self.__targets
